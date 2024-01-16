# Generated by Django 5.0.1 on 2024-01-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_url", models.URLField(max_length=256)),
                ("time_date_created", models.DateTimeField()),
                ("shot_url", models.CharField(max_length=64)),
            ],
        ),
    ]
