from rest_framework import serializers

from core.models import OrderMessage


class OrderMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMessage
        fields = '__all__'
        depth = 1