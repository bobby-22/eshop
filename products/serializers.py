from django.http import request
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
            "category",
            "date",
            "user",
            "description",
            "stripe_product_id",
            "stripe_price_id",
        )


class ProductNewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=50,
        required=True,
        error_messages={
            "blank": "Title cannot be empty",
            "max_length": "Title cannot be longer than 50 characters",
        },
    )
    price = serializers.IntegerField(
        required=True,
        error_messages={
            "blank": "Price cannot be empty",
        },
    )
    country = serializers.CharField(
        max_length=25,
        required=True,
        error_messages={
            "blank": "Country cannot be empty",
            "max_length": "Country cannot be longer than 25 characters",
        },
    )
    category = serializers.CharField(
        max_length=25,
        required=True,
        error_messages={
            "blank": "Category cannot be empty",
            "max_length": "Category cannot be longer than 25 characters",
        },
    )
    description = serializers.CharField(
        max_length=500,
        required=True,
        error_messages={
            "blank": "Description cannot be empty",
            "max_length": "Description cannot be longer than 500 characters",
        },
    )

    class Meta:
        model = ProductModel
        fields = (
            "title",
            "price",
            "country",
            "category",
            "owner",
            "description",
        )

    def create(self, validated_data):
        stripe_product = stripe.Product.create(
            name=validated_data["title"], description=validated_data["description"]
        )
        stripe_price = stripe.Price.create(
            product=stripe_product.id,
            currency="EUR",
            unit_amount=validated_data["price"] * 100,
        )
        product = ProductModel.objects.create(
            title=validated_data["title"],
            price=validated_data["price"],
            country=validated_data["country"],
            category=validated_data["category"],
            owner=validated_data["owner"],
            description=validated_data["description"],
            stripe_product_id=stripe_product.id,
            stripe_price_id=stripe_price.id,
        )
        return product
