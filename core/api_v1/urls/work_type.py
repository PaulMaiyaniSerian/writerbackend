from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.work_type import WorkTypeViewSet


router = DefaultRouter()
router.register(r'v1/work-types', WorkTypeViewSet, basename='work_type')


urlpatterns = [
    path('', include(router.urls)),
]