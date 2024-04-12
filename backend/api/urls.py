from django.urls import path

from .views import FaqAnswersListView, PartnerCompaniesListView, FaqQuestionView

urlpatterns = [
    path("faq-answers/", FaqAnswersListView.as_view()),
    path("partner-companies/", PartnerCompaniesListView.as_view()),
    path("faq-question/", FaqQuestionView.as_view()),
]
