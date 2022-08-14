from django.urls import path, include
from .views import RegisterUserApiView

urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name='register'),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
]