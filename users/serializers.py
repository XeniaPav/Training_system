from rest_framework.serializers import ModelSerializer
from users.models import User, UserBalance, Subscription


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = User
        fields = "__all__"


class UserBalanceSerializer(ModelSerializer):
    """Сериализатор для баланса пользователя"""

    class Meta:
        model = UserBalance
        fields = "__all__"
