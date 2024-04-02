from rest_framework import serializers
from .models import FaqAnswer, PartnerCompany, FaqQuestion


class FaqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAnswer
        fields = ["title", "content"]


class PartnerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerCompany
        fields = ["company_name", "company_logo", "company_website"]


class FaqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestion
        fields = "__all__"

