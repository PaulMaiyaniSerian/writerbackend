from django_filters import rest_framework as filters

from core.models import OrderMessage


class OrderMessageFilter(filters.FilterSet):
    class Meta:
        model = OrderMessage
        fields = '__all__'
