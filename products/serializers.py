from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth import get_user_model

User = get_user_model()
import stripe

from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    description = serializers.CharField(max_length=500, default="")
    category = serializers.CharField(max_length=25, default="")

    class Meta:
        model = ProductModel
        fields = ("title", "price", "country", "description", "category", "owner")

    def create(self, validated_data):
        stripe_product = stripe.Product.create(
            name=validated_data["title"],
            description=validated_data["description"]
        )
        stripe_price = stripe.Price.create(
            product=stripe_product.id,
            currency="CZK",
            unit_amount=validated_data["price"] * 100
        )
        product = ProductModel.objects.create(
            title=validated_data["title"],
            price=validated_data["price"],
            country=validated_data["country"],
            description=validated_data["description"],
            category=validated_data["category"],
            owner=validated_data["owner"],


            stripe_product_id=stripe_product.id,
            stripe_price_id=stripe_price.id
        )
        return product
