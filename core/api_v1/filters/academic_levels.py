from django_filters import rest_framework as filters

from core.models import AcademicLevel


class AcademicLevelFilter(filters.FilterSet):
    class Meta:
        model = AcademicLevel
        fields = '__all__'
