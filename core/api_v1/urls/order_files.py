from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.order_message import OrderFileViewSet


router = DefaultRouter()
router.register(r'v1/order-files', OrderFileViewSet, basename='order-files')


urlpatterns = [
    path('', include(router.urls)),
]