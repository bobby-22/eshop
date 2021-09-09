from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/latest/", views.LatestView.as_view()),
    path("product/<slug:stripe_product_id>/", views.DetailsView.as_view()),
    path("category/<slug:category>/", views.CategoryView.as_view()),
    path("search/", views.SearchView.as_view()),
    path("user/<int:user_id>", views.ProfileView.as_view()),
    path("product-create/", views.ProductNewView.as_view()),
    path("images-create/", views.ProductImagesNewView.as_view()),
    path("donate/", views.DonateView.as_view()),
    path("success/", views.success),
    path("cancel/", views.success)
]
