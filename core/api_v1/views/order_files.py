from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from core.api_v1.filters.order_files import OrderFileFilter
from core.api_v1.serializers.order_files import OrderFileSerializer
from core.models import OrderFile
from pagination import StandardResultsSetPagination

from rest_framework import filters


class OrderFileViewSet(ModelViewSet):
    # use filters too
    queryset = OrderFile.objects.all()
    serializer_class = OrderFileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields = ['name']
    filterset_class = OrderFileFilter
    pagination_class = StandardResultsSetPagination
