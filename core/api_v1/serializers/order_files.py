from rest_framework import serializers

from core.models import OrderFile


class OrderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFile
        fields = '__all__'
        depth = 1