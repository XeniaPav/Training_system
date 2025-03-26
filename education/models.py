from config import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название курса"
    )

    description = models.TextField(
        verbose_name="Описание", **NULLABLE, help_text="Введите описание продукта"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
        help_text="Укажите владельца продукта",
    )

    price = models.PositiveIntegerField(
        verbose_name="стоимость",
        help_text="Укажите стоимость продукта",
    )

    start_data = models.DateTimeField(
        verbose_name="Дата старта",
        **NULLABLE,
        help_text="Укажите владельца продукта",
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступен для покупки",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Lesson(models.Model):
    """Модель урока"""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Укажите курс урока",
    )

    title = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название урока"
    )

    url = models.CharField(
        max_length=100,
        verbose_name="Ссылка на урок",
        help_text="Введите ссылку на видео урока",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
