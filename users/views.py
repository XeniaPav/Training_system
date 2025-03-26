from decimal import Decimal

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from education.models import Product
from users.models import User, UserBalance, Subscription
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """вьюсет для модели пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    """контроллер для регистрации пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class SubscriptionCreateAPIView(CreateAPIView):
    """Контроллер для создания и удаления подписки"""

    def post(self, requests, product_id):
        user_balance = get_object_or_404(UserBalance, user=requests.user)
        product = get_object_or_404(Product, id=product_id)
        decimal_price = Decimal(product.price)
        if user_balance.balance < decimal_price:
            return Response(
                {"error": "Недостаточно бонусов"}, status=status.HTTP_400_BAD_REQUEST
            )
        subscription, created = Subscription.objects.get_or_create(
            user=requests.user, product=product
        )
        if created:
            user_balance.balance -= decimal_price
            user_balance.save()
            group_index = (
                subscription.group_index
                if hasattr(subscription, "group_index")
                else None
            )
            return Response(
                {
                    "massange": f"Оплата прошла успешно.Вы распределены в группу {group_index}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Подписка уже активна"}, status=status.HTTP_400_BAD_REQUEST
            )
