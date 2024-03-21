from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from accounts.api_v1.serializer.users import UserSerializer
from pagination import StandardResultsSetPagination

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

    filter_fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering_fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('username',)

    # ovveride delete method to prevent deletion of user instead set is_active to False
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_create(self, serializer):
        # create generate default password for user
        # and set email as username
        serializer.validated_data['email'] = serializer.validated_data.get('email', None) or serializer.validated_data.get(
            'username')
        if serializer.is_valid():
            user = serializer.save()
            user.set_password("password")
            user.save()




