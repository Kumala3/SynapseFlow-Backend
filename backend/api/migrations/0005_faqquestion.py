# Generated by Django 5.0.3 on 2024-04-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_insert_partners_companies_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqQuestion',
            fields=[
                ('question_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='FAQ ID')),
                ('email', models.TextField(max_length=100, verbose_name='Customer email')),
                ('question', models.TextField(max_length=1000, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
    ]