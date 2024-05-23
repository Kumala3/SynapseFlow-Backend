from django.test import TestCase
from api.models import (
    FaqAnswer,
    FaqQuestion,
    PartnerCompany,
    PricingPlan,
    PricingPlanAdvantage,
)


class FaqAnswerTest(TestCase):
    def setUp(self) -> None:
        self.faq_answer = FaqAnswer.objects.create(
            title="How long AI generates a response?",
            content="The response delivery depends on the request, but in generally, it doesn't take more than a few seconds.",
        )

    def test_faq_answer_creation(self):
        self.assertEqual(
            self.faq_answer.content,
            "The response delivery depends on the request, but in generally, it doesn't take more than a few seconds.",
        )
        self.assertEqual(self.faq_answer.title, "How long AI generates a response?")

    def test_faq_answer_str(self):
        self.assertEqual(
            str(self.faq_answer),
            f"The faq-answer-id: {self.faq_answer.answer_id};title: How long AI generates a response?",
        )


class FaqQuestionTest(TestCase):
    def setUp(self):
        self.faq_question = FaqQuestion.objects.create(
            email="kgroi332f@yahoo.com",
            question="How long could I ask the refund for a subscription after a purchase?",
        )

    def test_faq_question_creation(self):
        self.assertEqual(
            self.faq_question.question,
            "How long could I ask the refund for a subscription after a purchase?",
        )
        self.assertEqual(self.faq_question.email, "kgroi332f@yahoo.com")

    def test_faq_question_str(self):
        self.assertEqual(
            str(self.faq_question),
            f"The faq-question-id: {self.faq_question.question_id};email: {self.faq_question.email}",
        )


class PartnerCompanyTest(TestCase):
    def setUp(self):
        self.partner_company = PartnerCompany.objects.create(
            company_name="Google",
            company_logo="https://postimg.cc/68y5FvN0",
            company_website="https://about.google/",
        )

    def test_partner_company_creation(self):
        self.assertEqual(self.partner_company.company_name, "Google")
        self.assertEqual(
            self.partner_company.company_logo, "https://postimg.cc/68y5FvN0"
        )
        self.assertEqual(self.partner_company.company_website, "https://about.google/")

    def test_partner_company_str(self):
        self.assertEqual(
            str(self.partner_company),
            f"The partner-company-id: {self.partner_company.company_id};company_name: Google",
        )


class PricingPlanTest(TestCase):
    def setUp(self):
        self.pricing_plan = PricingPlan.objects.create(
            plan="Free",
            description="Free plan to get started",
            cost=0,
            button_text="Get started",
        )

    def test_pricing_plan_creation(self):
        self.assertEqual(self.pricing_plan.plan, "Free")
        self.assertEqual(self.pricing_plan.description, "Free plan to get started")
        self.assertEqual(self.pricing_plan.cost, 0)
        self.assertEqual(self.pricing_plan.button_text, "Get started")

    def test_pricing_plan_str(self):
        self.assertEqual(
            str(self.pricing_plan),
            f"Plan: {self.pricing_plan.plan}; Cost: {self.pricing_plan.cost}",
        )


class PricingPlanAdvantageTest(TestCase):
    def setUp(self):
        self.pricing_plan_advantage = PricingPlanAdvantage.objects.create(
            plan=PricingPlan.objects.create(
                plan="Free",
                description="Free plan to get started",
                cost=0,
                button_text="Get started",
            ),
            advantage="30 requests per day",
        )

    def test_pricing_plan_advantage_creation(self):
        self.assertEqual(self.pricing_plan_advantage.plan.plan, "Free")
        self.assertEqual(self.pricing_plan_advantage.advantage, "30 requests per day")

    def test_pricing_plan_advantage_str(self):
        self.assertEqual(
            str(self.pricing_plan_advantage),
            f"Plan: {self.pricing_plan_advantage.plan.plan}; Advantage: {self.pricing_plan_advantage.advantage}",
        )
