from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from PIL import Image

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class ProductModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default="")
    category = models.ForeignKey(CategoryModel, on_delete=CASCADE)
    stripe_product_id = models.CharField(blank=True, max_length=200, default="")
    stripe_price_id = models.CharField(blank=True, max_length=200, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"