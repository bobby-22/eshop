from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("latest/", views.LatestView.as_view()),
    path("product/<slug:stripe_product_id>/", views.DetailsView.as_view()),
    path("category/<int:category_id>", views.CategoryView.as_view()),
    path("", views.SearchView.as_view()),
    path("profile/", views.ProfileView.as_view()),
    path("donate/", views.DonateView.as_view()),
    path("success/", views.success),
    path("cancel/", views.success)
]
