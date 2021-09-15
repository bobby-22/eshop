from django.conf import settings
from rest_framework import serializers
from .models import ProductModel, ImageModel
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.utils.crypto import get_random_string

User = get_user_model()


class ProductModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="owner.username", read_only=True)
    date = serializers.DateTimeField(format="%d/%m/%Y")

    class Meta:
        model = ProductModel
        fields = "__all__"


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class ProductModelCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField(validators=[MaxValueValidator(9999)])
    country = serializers.CharField(max_length=25)
    category = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=1000)

    class Meta:
        model = ProductModel
        fields = "__all__"

    def create(self, validated_data):
        if self.context["request"].user != validated_data["owner"]:
            raise PermissionDenied()
        else:
            product = ProductModel.objects.create(
                title=validated_data["title"],
                price=validated_data["price"],
                country=validated_data["country"],
                category=validated_data["category"],
                owner=validated_data["owner"],
                description=validated_data["description"],
                thumbnail=validated_data["thumbnail"],
                post_id="post_" + get_random_string(length=30),
            )
            return product


class ImageModelCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.FileField())

    class Meta:
        model = ImageModel
        fields = "__all__"

    def create(self, validated_data):
        if self.context["request"].user != validated_data["owner"]:
            raise PermissionDenied()
        else:
            for image in validated_data.pop("images"):
                images = ImageModel.objects.create(
                    owner=validated_data["owner"],
                    post_id=validated_data["post_id"],
                    images=image,
                )
            return images


class ProductModelUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    price = serializers.IntegerField(validators=[MaxValueValidator(9999)])
    country = serializers.CharField(max_length=25)
    category = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=1000)
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = ProductModel
        fields = "__all__"
