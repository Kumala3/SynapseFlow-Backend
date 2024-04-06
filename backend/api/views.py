import logging
import betterlogging as bl

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from .models import FaqAnswer, PartnerCompany, FaqQuestion
from .serializers import FaqAnswerSerializer, PartnerCompanySerializer, FaqQuestionSerializer

log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


class FaqAnswersListView(APIView):
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
    def get(self, request: Request):
        return Response(
            status=status.HTTP_200_OK,
            data={"message": "This is the faq-question view"},
        )

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
                    data={"message": serializer.errors},
                )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )
