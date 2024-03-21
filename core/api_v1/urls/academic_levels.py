from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.academic_levels import AcademicLevelViewSet


router = DefaultRouter()
router.register(r'v1/work-types', AcademicLevelViewSet, basename='academic_levels')


urlpatterns = [
    path('', include(router.urls)),
]