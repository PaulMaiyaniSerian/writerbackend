from django_filters import rest_framework as filters

from core.models import OrderFile


class OrderFileFilter(filters.FilterSet):
    class Meta:
        model = OrderFile
        fields = ['order', 'creator']