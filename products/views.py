from django.shortcuts import render, redirect
from django.conf import settings
from products.models import ProductModel, ImageModel, ReviewModel, SavedModel
from django.contrib.auth import get_user_model
from products.serializers import (
    UserModelSerializer,
    ProductModelSerializer,
    ImageModelSerializer,
    ReviewModelSerializer,
    SavedModelSerializer,
    ProductModelCreateSerializer,
    ImageModelCreateSerializer,
    ReviewModelCreateSerializer,
    SavedModelCreateSerializer,
    ProductModelUpdateSerializer,
)
from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerOrReadOnly
from django.core.mail import send_mail

User = get_user_model()

# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 21


class LatestView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = CustomPagination


class Details1View(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        details = ProductModel.objects.filter(post_id=post_id)
        return details


class Details2View(generics.ListAPIView):
    serializer_class = ImageModelSerializer

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        images = ImageModel.objects.filter(post_id=post_id)
        return images


class CategoryView(generics.ListAPIView):
    serializer_class = ProductModelSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category = self.kwargs["category"]
        products = ProductModel.objects.filter(category=category)
        return products


class SearchView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "country", "description"]
    pagination_class = CustomPagination


class ProfileView(generics.ListAPIView):
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        products = ProductModel.objects.filter(owner=user)
        return products


class UserView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        user = User.objects.get(username=username)
        products = ProductModel.objects.filter(owner=user.id)
        return products


class ReviewView(generics.ListAPIView):
    serializer_class = ReviewModelSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        user = User.objects.get(username=username)
        reviews = ReviewModel.objects.filter(owner=user.id)
        return reviews


class SavedView(generics.ListAPIView):
    serializer_class = SavedModelSerializer

    def get_queryset(self):
        saved_products = SavedModel.objects.filter(post_id=self.kwargs["post_id"])
        return saved_products


class DateJoinedView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProductModelCreateView(generics.CreateAPIView):
    serializer_class = ProductModelCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ImageModelCreateView(generics.CreateAPIView):
    serializer_class = ImageModelCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ReviewModelCreateView(generics.CreateAPIView):
    serializer_class = ReviewModelCreateSerializer
    permission_classes = [IsAuthenticated]


class SavedModelCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SavedModelCreateSerializer


class ProductModelUpdateView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelUpdateSerializer
    lookup_field = "post_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProductModelDeleteView(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    lookup_field = "post_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        product = ProductModel.objects.get(post_id=post_id)
        self.check_object_permissions(self.request, product)
        product.delete()
        images = ImageModel.objects.filter(post_id=post_id)
        for image in images:
            self.check_object_permissions(self.request, image)
        images.delete()


class ImageModelDeleteView(generics.DestroyAPIView):
    queryset = ImageModel.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class SavedModelDeleteView(generics.DestroyAPIView):
    queryset = SavedModel.objects.all()
    lookup_field = "post_id"
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        saved_product = SavedModel.objects.get(post_id=post_id)
        self.check_object_permissions(self.request, saved_product)
        saved_product.delete()


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        owner = User.objects.get(username=username)
        send_mail(
            subject="MechMarketEU - Somebody is interested in your post",
            message=request.data.get("description")
            + "\n"
            + "\nPlease contact me at this email adress: "
            + request.data.get("email")
            + "\n\nThis e-mail was automatically sent, please do not reply back.",
            from_email="noreply.mechmarketeu@gmail.com",
            recipient_list=[owner.email],
            fail_silently=False,
        )
        return Response("Message has been successfully sent")


class ContactAdminView(APIView):
    def post(self, request):
        owner = User.objects.get(username="long")
        send_mail(
            subject="MechMarketEU - Feedback",
            message=request.data.get("description")
            + "\n"
            + "\nPlease contact me at this email adress: "
            + request.data.get("email"),
            from_email=request.data.get("email"),
            recipient_list=[owner.email],
            fail_silently=False,
        )
        return Response("Message has been successfully sent")
