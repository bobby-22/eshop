from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    country = models.CharField(max_length=25, default="")
    category = models.CharField(max_length=25, default="")
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to="images/")
    stripe_product_id = models.SlugField(max_length=100, default="")
    stripe_price_id = models.SlugField(max_length=100, default="")

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-date",)


class ImageModel(models.Model):
    stripe_product_id = models.SlugField(max_length=100, default="")
    images = models.FileField(upload_to="images/")

    class Meta:
        verbose_name_plural = "Media"
