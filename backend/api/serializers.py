from rest_framework import serializers
from .models import (
    FaqAnswer,
    PartnerCompany,
    FaqQuestion,
    PricingPlan,
    PricingPlanAdvantage,
)

from email_validator import validate_email as validate_email_address, EmailNotValidError


class FaqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAnswer
        fields = ["title", "content"]


class FaqQuestionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    question = serializers.CharField(max_length=800)

    class Meta:
        model = FaqQuestion
        fields = ["question", "email"]

    def validate_email(self, value):
        try:
            valid = validate_email_address(value)
            email = valid.email
        except EmailNotValidError as e:
            raise serializers.ValidationError(str(e))
        return email

    def validate_question(self, question):
        if len(question) < 50 or len(question) > 800:
            raise serializers.ValidationError(
                "Question must be at least 50 characters and no more than 800 characters"
            )
        return question

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
