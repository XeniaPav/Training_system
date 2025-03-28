# Generated by Django 5.1.7 on 2025-03-26 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_remove_user_username_user_phone_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserGroup",
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
                (
                    "group_number",
                    models.IntegerField(
                        help_text="Укажите номер группы", verbose_name="Номер группы"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
    ]
