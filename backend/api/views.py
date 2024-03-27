from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request


class FaqQuestion(APIView):
    def get(self, request: Request):
        return Response(status=status.HTTP_200_OK, data={"message": "Hello, world!"})
