from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="images/")
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, default="")
    price = models.IntegerField(default="")
    description = models.TextField(default="")
    image = models.FileField(upload_to="images/")
    category = models.ForeignKey(CategoryModel, related_name="products", on_delete=CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_product_id = models.SlugField(max_length=200, default="")
    stripe_price_id = models.SlugField(max_length=200, default="")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-date",)
