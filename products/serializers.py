from rest_framework import serializers
from .models import ProductModel


class ProductModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="owner.username", read_only=True)
    date = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = ProductModel
        fields = (
            "thumbnail",
            "image",
            "name",
            "price",
            "location",
            "date",
            "user",
            "description",
            "category",
            "stripe_product_id",
            "stripe_price_id",
        )
