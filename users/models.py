from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from education.models import NULLABLE, Product


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите e-mail"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserBalance(models.Model):
    """Модель баланса пользователя"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        **NULLABLE,
        help_text="Укажите пользователя",
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000,
    )

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("Баланс не может быть меньше 0")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}  - Баланс {self.balance}"

    class Meta:
        verbose_name = "Баланс"
        verbose_name_plural = "Баланс"


class Subscription(models.Model):
    """Модель подписки пользователя на курс"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        **NULLABLE,
        help_text="Укажите пользователя",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс",
    )

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class UserGroup(models.Model):
    """Модель учебной группы"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        **NULLABLE,
        help_text="Укажите пользователя",
    )

    group_number = models.IntegerField(
        verbose_name="Номер группы",
        help_text="Укажите номер группы",
    )
