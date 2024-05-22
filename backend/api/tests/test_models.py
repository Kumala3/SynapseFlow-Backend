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
        FaqAnswer.objects.create(
            title="How long AI generates a response?",
            content="The response delivery depends on the request, but in generally, it doesn't take more than a few seconds. ",
        )

    def test_faq_answer(self):
        faq_answer = FaqAnswer.objects.get(title="How long AI generates a response?")

        self.assertEqual(
            faq_answer.content,
            "The response delivery depends on the request, but in generally, it doesn't take more than a few seconds.",
        )
        self.assertEqual(faq_answer.title, "How long AI generates a response?")

    def test_faq_answer_str(self):
        faq_answer = FaqAnswer.objects.get(title="How long AI generates a response?")
        self.assertEqual(
            str(faq_answer),
            f"The faq-answer-id: {faq_answer.answer_id};title: How long AI generates a response?",
        )
