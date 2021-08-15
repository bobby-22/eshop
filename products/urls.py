from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("category/cables/", views.cables, name="cables"),
    path("category/deskmats/", views.deskmats, name="deskmats"),
    path("category/keyboards/", views.keyboards, name="keyboards"),
    path("category/keycaps/", views.keycaps, name="keycaps"),
    path("category/switches/", views.switches, name="switches"),
    path("category/others/", views.others, name="others"),
    path("product_create/", views.ProductCreate.as_view(), name="product_create"),
    path("latest/", views.latest, name="latest"),
    path("<slug:stripe_product_id>/", views.ProductDetails.as_view(), name="product_details"),
    path("donate/", views.Donate.as_view(), name="donate"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
]