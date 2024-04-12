from rest_framework import serializers
from .models import FaqAnswer, PartnerCompany, FaqQuestion


class FaqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAnswer
        fields = ["title", "content"]


class FaqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestion
        fields = ["question", "email"]

    def create(self, validated_data):
        return FaqQuestion.objects.create(**validated_data)


class PartnerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerCompany
        fields = ["company_name", "company_logo", "company_website"]


class FaqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqQuestion
        fields = ["question", "email"]

    def create(self, validated_data):
        return FaqQuestion.objects.create(**validated_data)
