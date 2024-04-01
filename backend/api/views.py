import logging
import betterlogging as bl

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from .models import FaqAnswer, PartnerCompany
from .serializers import FaqAnswerSerializer, PartnerCompanySerializer

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
                logger.info("No faq-answers found")
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
                logger.info("No partner-companies found")
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
