from rest_framework import serializers
from .models import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["name", "description", "thumbnail", "image", "price", "category", "stripe_product_id", "stripe_price_id"]
        