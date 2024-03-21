from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from core.api_v1.filters.academic_levels import AcademicLevelFilter
from core.api_v1.serializers.academic_levels import AcademicLevelSerializer
from core.models import WorkType, AcademicLevel
from pagination import StandardResultsSetPagination

from rest_framework import filters


class AcademicLevelViewSet(ModelViewSet):
    # use filters too
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_class = AcademicLevelFilter
    pagination_class = StandardResultsSetPagination
