from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import MyUser
from .serializers import UserRegistrationSerializer, UserListSerializer
from django.http import HttpResponse
def dashboard(request):
    return HttpResponse("<h1>Hello World</h1>")

class RegisterUserApiView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserListApi(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]