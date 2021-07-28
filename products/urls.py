from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("checkout_session/", views.CheckoutSession.as_view(), name="checkout_session"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
    path("add_product", views.ProductCreate.as_view(), name="add_product")
]