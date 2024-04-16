import logging
import betterlogging as bl

from rest_framework import serializers
from .models import (
    FaqAnswer,
    PartnerCompany,
    FaqQuestion,
    PricingPlan,
    PricingPlanAdvantage,
)

from email_validator import (
    validate_email as validate_email_address,
    EmailNotValidError,
)

log_level = logging.INFO
bl.basic_colorized_config(level=log_level)
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


class FaqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqAnswer
        fields = ["title", "content"]


class FaqQuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the FaqQuestion model.

    This serializer is used to validate and serialize FaqQuestion objects.
    It provides validation for the 'email' and 'question' fields, and also
    defines the fields to be included in the serialized representation.

    Attributes:
        email (serializers.EmailField): Field for the email address.
        question (serializers.CharField): Field for the question text.

    Methods:
        validate_email(value): Validates the email address.
        validate_question(question): Validates the question text.
        create(validated_data): Creates a new FaqQuestion object.

    """

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
            logger.error(f"Email validation error: {e}")
            raise serializers.ValidationError("Invalid email address")
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
