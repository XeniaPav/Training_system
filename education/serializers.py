from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, IntegerField
from education.models import Product, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    """Сериализатор для продукта"""

    class Meta:
        model = Product
        fields = "__all__"

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    def get_lessons_count(self, obj):
        """возвращает lessons_count - количество уроков в курсе"""
        if obj.lesson_set.all().count():
            return obj.lesson_set.all().count()
        else:
            return 0
