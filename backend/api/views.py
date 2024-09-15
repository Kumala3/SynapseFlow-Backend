import logging
import betterlogging as bl

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.exceptions import Throttled

from .throttles import FaqQuestionAnonRateThrottle, FaqQuestionRateThrottle
from .models import FaqAnswer, PartnerCompany, PricingPlan
from .serializers import (
    FaqAnswerSerializer,
    PartnerCompanySerializer,
    FaqQuestionSerializer,
    PricingPlanSerializer,
)

log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


class FaqAnswersListView(APIView):
    """
    View to retrieve a list of FAQ answers.

    Methods:
        - get: Retrieves all FAQ answers and returns them in the response like a list.
    """

    def get(self, request: Request):
        try:
            answers = FaqAnswer.objects.all()

            if not answers.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"message": "No answers found"},
                )
            else:
                serializer = FaqAnswerSerializer(answers, many=True)
                return Response(
                    status=status.HTTP_200_OK,
                    data={"answers": serializer.data},
                )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )


class PartnerCompaniesListView(APIView):
    """
    View to retrieve a list of partner companies.

    Methods:
        - get: Retrieves all partner companies and returns them in the response like a list.
    """
    def get(self, request: Request):
        try:
            partner_companies = PartnerCompany.objects.all()

            if not partner_companies.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"message": "No partner-companies found"},
                )
            else:
                serializer = PartnerCompanySerializer(partner_companies, many=True)

                return Response(
                    status=status.HTTP_200_OK,
                    data={"partner_companies": serializer.data},
                )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )


class FaqQuestionView(APIView):
    """
    View for handling FaQ question submissions.

    This view allows users to submit a question along with their email address.
    The question and email are validated and saved using the FaqQuestionSerializer.
    If the submission is successful, a success response is returned.
    If there are any validation errors or exceptions occur, appropriate error responses are returned.

    Methods:
        - post(request: Request) -> Response: Handles the question submission.
    """

    throttle_classes = [FaqQuestionRateThrottle, FaqQuestionAnonRateThrottle]

    def post(self, request: Request):
        try:
            question = request.data.get("question")
            email = request.data.get("email")

            if not question or not email:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"message": "Please provide question and email"},
                )

            data = {
                "question": question,
                "email": email,
            }

            serializer = FaqQuestionSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    status=status.HTTP_201_CREATED,
                    data={"status": "success"},
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"status": "failure", "error_messages": serializer.errors},
                )
        except Throttled as exc:
            wait = exc.wait()
            logger.warning(f"Rate limit exceeded. Try again in {wait} seconds.")
            return Response(
                status=status.HTTP_429_TOO_MANY_REQUESTS,
                data={"message": f"Rate limit exceeded. Try again in {wait} seconds."},
            )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )


class PricingPlansView(APIView):
    """
    A view for retrieving pricing plans.

    This view handles GET requests and returns a list of pricing plans
    available in the system. If no pricing plans are found, a 404 response
    is returned. If an error occurs during the retrieval process, a 500
    response is returned.

    Methods:
        get(request: Request) -> Response: Retrieves the pricing plans.
    """
    def get(self, request: Request):
        try:
            pricing_plan = PricingPlan.objects.all()

            if not pricing_plan.exists():
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"message": "No pricing-plans found"},
                )
            else:
                serializer = PricingPlanSerializer(pricing_plan, many=True)
                return Response(
                    status=status.HTTP_200_OK,
                    data={"pricing_plans": serializer.data},
                )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )
