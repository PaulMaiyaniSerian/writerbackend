from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from core.api_v1.filters.work_type import WorkTypeFilter
from core.api_v1.serializers.work_type import WorkTypeSerializer
from core.models import WorkType
from pagination import StandardResultsSetPagination

from rest_framework import filters


class WorkTypeViewSet(ModelViewSet):
    # use filters too
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_class = WorkTypeFilter
    pagination_class = StandardResultsSetPagination
