from django.contrib import admin

from .models import FaqAnswer, PartnerCompany, FaqQuestion

@admin.register(FaqAnswer)
class FaqAnswersAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ["company_name", "company_logo", "company_website"]


@admin.register(FaqQuestion)
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ["email", "question", "created_at"]
