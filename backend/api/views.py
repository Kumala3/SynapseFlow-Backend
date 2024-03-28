import logging
import betterlogging as bl

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

from .models import FaqAnswer

log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


class FaqQuestion(APIView):
    def get(self, request: Request):
        return Response(status=status.HTTP_200_OK, data={"message": "Hello, world!"})


class FaqAnswersList(APIView):
    def get(self, request: Request):
        try:
            answers = FaqAnswer.objects.all()

            if not answers:
                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={"message": "No answers found"},
                )
            else:
                return Response(
                    status=status.HTTP_200_OK,
                    data={"answers": answers},
                )
        except Exception as e:
            logger.error(f"Something went wrong, error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"message": "Internal server error"},
            )
