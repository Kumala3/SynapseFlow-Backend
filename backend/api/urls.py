from django.urls import path

from .views import FaqQuestion

urlpatterns = [
    path("faq-question/", FaqQuestion.as_view()),
    
]
