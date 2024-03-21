from django.contrib.auth import get_user_model
from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from accounts.api_v1.serializer.users import UserSerializer
from core.api_v1.filters.orders import OrderFilter
from core.api_v1.serializers.orders import OrderSerializer
from core.models import Order
from pagination import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import filters

User = get_user_model()


class OrderViewSet(ModelViewSet):
    # use filters too
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']
    filterset_class = OrderFilter
    pagination_class = StandardResultsSetPagination

