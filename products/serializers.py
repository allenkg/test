from rest_framework import serializers

from products.models import Category, Product, ProductHistory


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description',)


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()
    description = serializers.SerializerMethodField()

    @staticmethod
    def get_description(obj):
        return obj.description[:100] if getattr(obj, 'description') else None

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'product_count')


class ProductHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHistory
        fields = ('id', 'product_data', 'product', 'created_at')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'qty')


class ProductRetrieveSerializer(ProductSerializer):
    history = serializers.SerializerMethodField(required=False, read_only=True)

    @staticmethod
    def get_history(obj):
        return ProductHistorySerializer(obj.producthistory_set.all(), many=True).data

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ('history',)

