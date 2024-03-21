from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api_v1.views.order_message import OrderMessageViewSet


router = DefaultRouter()
router.register(r'v1/order-messages', OrderMessageViewSet, basename='order_messages')


urlpatterns = [
    path('', include(router.urls)),
]