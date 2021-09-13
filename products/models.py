from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from rest_framework.compat import md_filter_add_syntax_highlight

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=40, default="")
    price = models.IntegerField(default="")
    country = models.CharField(max_length=20, default="")
    category = models.CharField(max_length=20, default="")
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default="")
    thumbnail = models.FileField(max_length=200, upload_to="thumbnails/")
    stripe_product_id = models.SlugField(max_length=100, default="")
    stripe_price_id = models.SlugField(max_length=100, default="")

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-id",)


class ImageModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_product_id = models.SlugField(max_length=100, default="")
    images = models.FileField(max_length=200, upload_to="images/")

    class Meta:
        verbose_name_plural = "Media"
