from django.urls import path
from education.apps import EducationConfig
from education.views import ProductListView, LessonListAPIView

app_name = EducationConfig.name

urlpatterns = [
    path("product/", ProductListView.as_view(), name="product-list"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
]
