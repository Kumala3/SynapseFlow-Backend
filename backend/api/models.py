from django.db import models

class FaqAnswer(models.Model):
    answer_id = models.BigAutoField(verbose_name="FAQ ID", primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Title")
    answer = models.TextField(max_length=1000, verbose_name="Answer")
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
