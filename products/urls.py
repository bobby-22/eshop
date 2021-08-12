from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("cables/", views.cables, name="cables"),
    path("deskmats/", views.deskmats, name="deskmats"),
    path("keyboards/", views.keyboards, name="keyboards"),
    path("keycaps/", views.keycaps, name="keycaps"),
    path("switches/", views.switches, name="switches"),
    path("others/", views.others, name="others"),
    path("product_create/", views.ProductCreate.as_view(), name="product_create"),
    path("product_read/", views.product_read, name="product_read"),
    path("product_details/<slug:stripe_product_id>/", views.product_details, name="product_details"),
    path("product_update/<slug:stripe_product_id>/", views.ProductUpdate.as_view(), name="product_update"),
    path("product_delete/<slug:stripe_product_id>/", views.product_delete, name="product_delete"),
    path("donate/", views.Donate.as_view(), name="donate"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
]