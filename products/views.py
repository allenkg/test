from django.db.models import Count
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer, CategoryCreateSerializer, \
    ProductRetrieveSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(product_count=Count('product'))
        return qs

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return self.serializer_class
        return CategoryCreateSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductRetrieveSerializer
        return self.serializer_class
