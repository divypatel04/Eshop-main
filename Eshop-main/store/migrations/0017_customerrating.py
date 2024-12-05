# Generated by Django 5.1.3 on 2024-11-19 19:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0016_roommember_meeting_date_meeting_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerRating",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stars", models.IntegerField(default=0)),
                ("comment", models.TextField(blank=True, null=True)),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "rated_customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_ratings",
                        to="store.customer",
                    ),
                ),
                (
                    "rater",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="given_ratings",
                        to="store.customer",
                    ),
                ),
            ],
        ),
    ]