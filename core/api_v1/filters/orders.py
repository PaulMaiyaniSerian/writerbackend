from django_filters import rest_framework as filters

from core.models import Order


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'

