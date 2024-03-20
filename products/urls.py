from django.urls import include, path
from rest_framework import routers

from products.views import CategoriesViewSet, ProductViewSet

app_name = 'products'

router = routers.SimpleRouter()

router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]