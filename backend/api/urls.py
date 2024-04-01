from django.urls import path

from .views import FaqAnswersListView, PartnerCompaniesListView

urlpatterns = [
    path("faq-answers/", FaqAnswersListView.as_view()),
    path("partner-companies/", PartnerCompaniesListView.as_view()),
]
