from django.urls import path

from .views import FaqQuestion, FaqAnswersList, PartnerCompaniesView

urlpatterns = [
    path("faq-question/", FaqQuestion.as_view()),
    path("faq-answers/", FaqAnswersList.as_view()),
    path("partner-companies/", PartnerCompaniesView.as_view()),
]
