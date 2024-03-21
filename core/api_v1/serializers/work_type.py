from rest_framework import serializers

from core.models import WorkType


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'
        depth = 1