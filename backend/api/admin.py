from django.contrib import admin

from .models import FaqAnswer, PartnerCompany, PricingPlan, PricingPlanAdvantage


@admin.register(FaqAnswer)
class FaqAnswersAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ["company_name", "company_logo", "company_website"]


@admin.register(PricingPlan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["plan", "description", "cost", "button_text"]


@admin.register(PricingPlanAdvantage)
class PlanAdvantageAdmin(admin.ModelAdmin):
    list_display = ["plan", "advantage"]
