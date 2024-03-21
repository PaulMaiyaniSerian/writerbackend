from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.orders import OrderViewSet


router = DefaultRouter()
router.register(r'v1/orders', OrderViewSet, basename='orders')


urlpatterns = [
    path('', include(router.urls)),
]
