from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, UserBalance, Subscription, UserGroup


@receiver(post_save, sender=User)
def create_user_balance(sender, instance, created, **kwargs):
    """Создание баланса пользователя при регистрации нового пользователя"""
    if created:
        UserBalance.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_balance(sender, instance, created, **kwargs):
    """Сохранение баланса пользователя при регистрации нового пользователя"""
    if hasattr(instance, "userbalance"):
        instance.userbalance.save()


@receiver(post_save, sender=Subscription)
def distribute_user_to_groups(sender, instance, created, **kwargs):
    """Распреденление пользователя в группы"""

    if created:
        subscriptions = Subscription.objects.filter(product=instance.product)
        group = [[] for _ in range(10)]
        for i, subscription in enumerate(subscriptions):
            group_index = i % 10
            group[group_index].append(subscription.user)
            UserGroup.objects.update_or_create(
                user=subscription.user, defaults={"group_number": group_index + 1}
            )
            if subscription == instance:  # Если это текущая подписка
                instance.group_index = group_index + 1  # Сохраняем номер группы
