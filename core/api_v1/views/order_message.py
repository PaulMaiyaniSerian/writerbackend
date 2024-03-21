from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from core.api_v1.filters.order_message import OrderMessageFilter
from core.api_v1.serializers.order_message import OrderMessageSerializer
from core.models import OrderMessage
from pagination import StandardResultsSetPagination

from rest_framework import filters


class OrderMessageViewSet(ModelViewSet):
    # use filters too
    queryset = OrderMessage.objects.all()
    serializer_class = OrderMessageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_class = OrderMessageFilter
    pagination_class = StandardResultsSetPagination
