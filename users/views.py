from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserRegisterSerializer
from users.utils import create_user_tokens


class UserViewSet(GenericViewSet):
    pass


class LoginApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        token = create_user_tokens(user)
        return Response({'token': token['access']})


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)