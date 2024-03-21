from django_filters import rest_framework as filters

from core.models import Subject


class SubjectFilter(filters.FilterSet):
    class Meta:
        model = Subject
        fields = '__all__'
