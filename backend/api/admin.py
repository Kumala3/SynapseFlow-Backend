from django.contrib import admin

from .models import FaqAnswer

@admin.register(FaqAnswer)
class FaqAnswersAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
