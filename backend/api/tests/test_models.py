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
