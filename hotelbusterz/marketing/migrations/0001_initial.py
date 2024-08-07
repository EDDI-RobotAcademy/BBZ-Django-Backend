# Generated by Django 5.0.6 on 2024-07-05 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0002_accountlog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marketing",
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
                ("acquisition", models.PositiveIntegerField()),
                ("activation", models.PositiveIntegerField()),
                ("revenue", models.PositiveIntegerField()),
                ("retention", models.PositiveIntegerField()),
                ("referral", models.PositiveIntegerField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "marketing",
            },
        ),
    ]
