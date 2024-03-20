from django.urls import include, path
from rest_framework import routers

from users.views import UserViewSet, LoginApiView, RegisterApiView

app_name = 'users'

router = routers.SimpleRouter()

router.register(r'current', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
]
