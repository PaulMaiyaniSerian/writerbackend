from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.subjects import SubjectViewSet


router = DefaultRouter()
router.register(r'v1/subjects', SubjectViewSet, basename='subjects')


urlpatterns = [
    path('', include(router.urls)),
]