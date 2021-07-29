from collections import namedtuple
from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
    path("product_create", views.ProductCreate.as_view(), name="product_create"),
    path("product_read", views.product_read, name="product_read"),
    path("product_details/<int:product_id>", views.product_details, name="product_details"),
    path("checkout_session/", views.CheckoutSession.as_view(), name="checkout_session"),
]