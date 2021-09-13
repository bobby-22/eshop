from django.shortcuts import render, redirect
from django.conf import settings
from products import serializers
from products.models import ProductModel, ImageModel
from django.contrib.auth import get_user_model
from products.serializers import (
    ProductModelSerializer,
    ImageModelSerializer,
    ProductModelCreateSerializer,
    ImageModelCreateSerializer,
    ProductModelUpdateSerializer,
)
from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.core.mail import send_mail

import stripe

User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
class LatestView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


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
    search_fields = ["title", "country", "description"]


class ProfileView(generics.ListAPIView):
    serializer_class = ProductModelSerializer
    lookup_field = "profile_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        profile_id = self.kwargs["profile_id"]
        products = ProductModel.objects.filter(owner=profile_id)
        # for product in products:
        #     self.check_object_permissions(self.request, product)
        return products


class UserView(generics.ListAPIView):
    serializer_class = ProductModelSerializer
    lookup_field = "username"

    def get_queryset(self):
        username = self.kwargs["username"]
        user_id = User.objects.get(username=username)
        products = ProductModel.objects.filter(owner=user_id)
        return products


class ProductModelCreateView(generics.CreateAPIView):
    serializer_class = ProductModelCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ImageModelCreateView(generics.CreateAPIView):
    serializer_class = ImageModelCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProductModelUpdateView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelUpdateSerializer
    lookup_field = "stripe_product_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProductModelDeleteView(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    lookup_field = "stripe_product_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        stripe_product_id = self.kwargs["stripe_product_id"]
        stripe.Product.modify(stripe_product_id, active="false")
        product = ProductModel.objects.get(stripe_product_id=stripe_product_id)
        self.check_object_permissions(self.request, product)
        product.delete()
        images = ImageModel.objects.filter(stripe_product_id=stripe_product_id)
        for image in images:
            self.check_object_permissions(self.request, image)
        images.delete()


class ImageModelDeleteView(generics.DestroyAPIView):
    queryset = ImageModel.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        owner = User.objects.get(id=request.data.get("owner"))
        send_mail(
            subject="MechMarketEU - Somebody is interested in your product",
            message=request.data.get("description")
            + "\n"
            + "\nPlease contact me at this email adress: "
            + request.data.get("email"),
            from_email="noreply.mechmarketeu@gmail.com",
            recipient_list=[owner.email],
            fail_silently=False,
        )
        return Response("Message has been successfully sent")


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
