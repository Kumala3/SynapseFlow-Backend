from rest_framework import serializers
from .models import FaqAnswer


class FaqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAnswer
        fields = "__all__"
