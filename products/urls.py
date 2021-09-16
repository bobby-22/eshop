from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/latest/", views.LatestView.as_view()),
    path("products/<slug:post_id>/details/", views.Details1View.as_view()),
    path("products/<slug:post_id>/images/", views.Details2View.as_view()),
    path("products/category/<slug:category>/", views.CategoryView.as_view()),
    path("products/search/", views.SearchView.as_view()),
    path("accounts/profile/", views.ProfileView.as_view()),
    path("accounts/user/<slug:username>", views.UserView.as_view()),
    path("products/create/", views.ProductModelCreateView.as_view()),
    path("images/create/", views.ImageModelCreateView.as_view()),
    path(
        "products/<slug:post_id>/update/",
        views.ProductModelUpdateView.as_view(),
    ),
    path(
        "products/<slug:post_id>/delete/",
        views.ProductModelDeleteView.as_view(),
    ),
    path(
        "images/<int:id>/delete/",
        views.ImageModelDeleteView.as_view(),
    ),
    path("accounts/user/<slug:username>/reviews/", views.ReviewView.as_view()),
    path("contact/user/", views.ContactView.as_view()),
    path("review/user/", views.ReviewModelCreateView.as_view()),
]
