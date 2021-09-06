from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="owner.username", read_only=True)
    date = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = ProductModel
        fields = (
            "thumbnail",
            "image",
            "title",
            "price",
            "country",
            "date",
            "user",
            "description",
            "category",
            "stripe_product_id",
            "stripe_price_id",
        )

class ProductNewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50, default="")
    price = serializers.IntegerField(default="")
    country = serializers.CharField(max_length=25, default="")

    class Meta:
        model = ProductModel
        fields = ("title", "price", "country")

    def create(self, validated_data):
        product = ProductModel.objects.create(
            title=validated_data["title"],
            price=validated_data["price"],
            country=validated_data["country"],
        )
        return product
