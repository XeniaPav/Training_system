from django.contrib import admin
from education.models import Product, Lesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("id", "title", "description", "owner", "price", "start_data")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ("id", "product", "title", "url")
