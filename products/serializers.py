from rest_framework import serializers
from .models import ProductModel, CategoryModel

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["name", "thumbnail", "date", "location", "price", "description", "image", "category", "owner", "stripe_product_id", "stripe_price_id"]

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]
