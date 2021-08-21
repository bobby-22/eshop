from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("latest/", views.Latest.as_view()),
    path("product/<slug:stripe_product_id>/", views.Details.as_view()),
    path("category/<int:category_id>", views.Category.as_view()),
    path("profile/", views.Profile.as_view()),
    path("donate/", views.Donate.as_view(), name="donate"),
    path("success/", views.success, name="success"),
    path("cancel/", views.success, name="cancel"),
]
