from django_filters import rest_framework as filters

from core.models import WorkType


class WorkTypeFilter(filters.FilterSet):
    class Meta:
        model = WorkType
        fields = '__all__'
