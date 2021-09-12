from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/latest/", views.LatestView.as_view()),
    path("products/<slug:stripe_product_id>/details/", views.Details1View.as_view()),
    path("products/<slug:stripe_product_id>/images/", views.Details2View.as_view()),
    path("products/category/<slug:category>/", views.CategoryView.as_view()),
    path("products/search/", views.SearchView.as_view()),
    path("accounts/profile/<int:profile_id>", views.ProfileView.as_view()),
    path("accounts/user/<slug:username>", views.UserView.as_view()),
    path("products/create/", views.ProductModelCreateView.as_view()),
    path("images/create/", views.ImageModelCreateView.as_view()),
    path(
        "products/<slug:stripe_product_id>/update/",
        views.ProductModelUpdateView.as_view(),
    ),
    path(
        "products/<slug:stripe_product_id>/delete/",
        views.ProductModelDeleteView.as_view(),
    ),
    path(
        "images/<int:id>/delete/",
        views.ImageModelDeleteView.as_view(),
    ),
    path("donate/", views.DonateView.as_view()),
    path("success/", views.success),
    path("cancel/", views.success),
]
