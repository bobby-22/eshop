from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from rest_framework.compat import md_filter_add_syntax_highlight

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    country = models.CharField(max_length=25, default="")
    category = models.CharField(max_length=25, default="")
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default="")
    thumbnail = models.FileField(max_length=200)
    post_id = models.SlugField(unique=True, default="")

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-id",)


class ImageModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.SlugField(default="")
    images = models.FileField(max_length=200)

    class Meta:
        verbose_name_plural = "Media"

class ReviewModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    reviewer = models.CharField(max_length=20, default="")
    rating = models.CharField(max_length=20, default="")
    description = models.TextField(max_length=1000, default="")

    class Meta:
        verbose_name_plural = "Reviews"
        ordering = ("-id",)