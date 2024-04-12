from rest_framework import serializers
from .models import (
    FaqAnswer,
    PartnerCompany,
    FaqQuestion,
    PricingPlan,
    PricingPlanAdvantage,
)


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


class PricingPlanAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlanAdvantage
        fields = ["advantage"]


class PricingPlanSerializer(serializers.ModelSerializer):
    advantages = PricingPlanAdvantageSerializer(many=True)

    class Meta:
        model = PricingPlan
        fields = ["plan", "description", "cost", "button_text", "advantages"]
