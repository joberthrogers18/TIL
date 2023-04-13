from django.urls import path
from .views import GroupViewSet, UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users'),
    path('groups/', GroupViewSet.as_view({'get': 'list'}), name='groups'),
]
