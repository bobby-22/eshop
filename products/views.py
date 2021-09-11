from django.shortcuts import render, redirect
from django.conf import settings
from products.models import ProductModel, ImageModel
from products.serializers import (
    ProductModelSerializer,
    ImageModelSerializer,
    ProductModelCreateSerializer,
    ImageModelCreateSerializer,
    ProductModelUpdateSerializer,
    ImageModelUpdateSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
class LatestView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated]


class Details1View(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        stripe_product_id = self.kwargs["stripe_product_id"]
        details = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        return details


class Details2View(generics.ListAPIView):
    serializer_class = ImageModelSerializer

    def get_queryset(self):
        stripe_product_id = self.kwargs["stripe_product_id"]
        images = ImageModel.objects.filter(stripe_product_id=stripe_product_id)
        return images


class CategoryView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        category = self.kwargs["category"]
        products = ProductModel.objects.filter(category=category)
        return products


class SearchView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "country"]


class ProfileView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        products = ProductModel.objects.filter(owner=user_id)
        return products


class ProductModelCreateView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelCreateSerializer


class ImageModelCreateView(generics.CreateAPIView):
    serializer_class = ImageModelCreateSerializer


class ProductModelDeleteView(APIView):
    def post(self, request, stripe_product_id):
        stripe.Product.modify(stripe_product_id, active="false")
        product = ProductModel.objects.filter(stripe_product_id=stripe_product_id)
        product.delete()
        images = ImageModel.objects.filter(stripe_product_id=stripe_product_id)
        images.delete()
        return Response("Product has been successfully deleted")


class ProductModelUpdateView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelUpdateSerializer

    def patch(self, request, instance):
        title = request.data.get("title")
        price = request.data.get("price")
        description = request.data.get("description")
        thumbnail = request.data.get("thumbnail")
        stripe_product_id = request.data.get("stripe_product_id")
        stripe_price_id = request.data.get("stripe_price_id")
        if "price" in instance.changed_data:
            stripe.Price.modify(stripe_price_id, active="false")
            price = stripe.Price.create(
                product=stripe_product_id,
                currency="EUR",
                unit_amount=price * 100,
            )
            stripe_price_id = price.id
        if "name" in instance.changed_data:
            stripe.Product.modify(stripe_product_id, name=title)
        if "description" in instance.changed_data:
            stripe.Product.modify(stripe_product_id, description=description)
        instance = self.get_object()
        instance.title = title
        instance.price = price
        instance.description = description
        instance.thumbnail = thumbnail
        instance.save()


class ImageModelUpdateView(generics.CreateAPIView):
    serializer_class = ImageModelUpdateSerializer


def success(request):
    return render(request, "products/success.html")


def cancel(request):
    return render(request, "products/cancel.html")


class DonateView(APIView):
    def post(self, request):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {"price": "price_1JNJftGipF6CtVMryAn0ON5T", "quantity": 1},
                {"price": "price_1JNJftGipF6CtVMrlCfxytYD", "quantity": 1},
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cancel",
        )
        return redirect(checkout_session.url, code=303)
