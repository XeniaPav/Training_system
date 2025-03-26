from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from education.models import Product, Lesson
from education.paginators import CustomPagination
from education.serializers import ProductSerializer, LessonSerializer
from users.models import Subscription


class ProductListView(generics.ListAPIView):
    """Список продуктов"""

    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination

    def get_queryset(self):
        products = Product.objects.all()
        user = self.request.user
        user_subscriptions = Subscription.objects.filter(user=user).values_list(
            "product_id", flat=True
        )
        available_products = products.exclude(id__in=user_subscriptions)
        return available_products


class LessonListAPIView(generics.ListAPIView):
    """Список уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination
