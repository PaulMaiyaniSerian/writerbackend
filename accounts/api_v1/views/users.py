from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from accounts.api_v1.filters.users import UserFilters
from accounts.api_v1.serializer.users import UserSerializer
from pagination import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = UserFilters
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
        serializer.validated_data['email'] = serializer.validated_data.get('email',
                                                                           None) or serializer.validated_data.get(
            'username')
        if serializer.is_valid():
            user = serializer.save()
            user.set_password("password")
            user.save()

    # action to list users with is_writer=True`
    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer(many=True),
        summary="list writers"
    )
    @action(detail=False, methods=['get'], url_path='list-writers', url_name='writers')
    def list_writers(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(is_writer=True)
        # apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # action to list users with is_admin=True`
    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer(many=True),
        summary="list admins"
    )
    @action(detail=False, methods=['get'], url_path='list-admins', url_name='admins')
    def list_admins(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(is_admin=True)
        # apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # action to list users with is_client=True`
    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer(many=True),
        summary="list clients"
    )
    @action(detail=False, methods=['get'], url_path='list-clients', url_name='clients')
    def list_clients(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(is_client=True)
        # apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)