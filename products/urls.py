from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
    path("profile/", views.profile, name="profile"),
    path("product_create/", views.ProductCreate.as_view(), name="product_create"),
    path("product_read/", views.product_read, name="product_read"),
    path("product_details/<slug:stripe_product_id>/", views.product_details, name="product_details"),
    path("product_update/<slug:stripe_product_id>/", views.ProductUpdate.as_view(), name="product_update"),
    path("product_delete/<slug:stripe_product_id>/", views.product_delete, name="product_delete"),
    path("checkout_session/", views.CheckoutSession.as_view(), name="checkout_session"),
]