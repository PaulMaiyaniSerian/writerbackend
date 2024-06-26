from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser',
            'first_name', 'last_name', 'is_writer', 'is_admin', 'is_client'
        ]
        depth = 1

