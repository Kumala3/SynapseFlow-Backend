from django.db import models

class FaqAnswer(models.Model):
    answer_id = models.BigAutoField(verbose_name="FAQ ID", primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(max_length=1000, verbose_name="Content")
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"The faq-answer-id: {self.answer_id};title: {self.title}"


class PartnerCompany(models.Model):
    company_id = models.BigAutoField(verbose_name="Company ID", primary_key=True)
    company_name = models.CharField(max_length=255, verbose_name="Company name")
    company_logo = models.URLField(verbose_name="Company logo")
    company_website = models.URLField(verbose_name="Company website")
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"The partner-company-id: {self.company_id};company_name: {self.company_name}"


class FaqQuestion(models.Model):
    question_id = models.BigAutoField(verbose_name="FAQ ID", primary_key=True)
    email = models.TextField(max_length=100, verbose_name="Customer email")
    question = models.TextField(max_length=1000, verbose_name="Content")
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return f"The faq-question-id: {self.question_id};email: {self.email}"
