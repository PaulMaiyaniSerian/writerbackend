# accounts/api_v1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.api_v1.views.users import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'v1/accounts', UserViewSet, basename='user')
# router.register(r'v1/manager', UserManagerViewSet, basename='user')
# router.register(r'v1/students', StudentProfileViewSet, basename='students'),
# router.register(r'v1/teachers', TeacherProfileViewSet, basename='teachers'),

urlpatterns = [
    path('', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
