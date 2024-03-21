from rest_framework import serializers

from core.models import AcademicLevel


class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'
        depth = 1