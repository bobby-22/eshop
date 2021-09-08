from django.conf import settings
from rest_framework import serializers
from .models import ProductModel, ImageModel
from django.contrib.auth import get_user_model
import stripe

User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ("stripe_product_id", "images")


class ProductModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="owner.username", read_only=True)
    date = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = ProductModel
        fields = (
            "title",
            "price",
            "country",
            "category",
            "date",
            "user",
            "description",
            "thumbnail",
            "stripe_product_id",
            "stripe_price_id",
        )


class ProductNewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    country = serializers.CharField(max_length=25)
    category = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=500)

    class Meta:
        model = ProductModel
        fields = (
            "title",
            "price",
            "country",
            "category",
            "owner",
            "description",
            "thumbnail",
            "stripe_product_id",
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
            thumbnail=validated_data["thumbnail"],
            stripe_product_id=stripe_product.id,
            stripe_price_id=stripe_price.id,
        )
        return product


class ProductImagesNewSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.FileField())

    class Meta:
        model = ImageModel
        fields = ("stripe_product_id", "images")

    def create(self, validated_data):
        for image in validated_data.pop("images"):
            images = ImageModel.objects.create(
                stripe_product_id=validated_data["stripe_product_id"], images=image
            )
        return images
