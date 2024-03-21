from django.contrib.auth import get_user_model
from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from core.api_v1.filters.subjects import SubjectFilter

from core.api_v1.serializers.subjects import SubjectSerializer
from core.models import Order, Subject
from pagination import StandardResultsSetPagination

from rest_framework import filters


class SubjectViewSet(ModelViewSet):
    # use filters too
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_class = SubjectFilter
    pagination_class = StandardResultsSetPagination

