from django.urls import path

from .views import FaqQuestion, FaqAnswersList

urlpatterns = [
    path("faq-question/", FaqQuestion.as_view()),
    path("faq-answers/", FaqAnswersList.as_view()),
]
