from django.contrib import admin
from users.models import User, UserBalance, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")


@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_filter = ("id", "user", "balance")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_filter = ("id", "user", "product")
