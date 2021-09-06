from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)


class ProductModel(models.Model):
    thumbnail = models.ImageField(upload_to="images/")
    image = models.FileField(upload_to="images/")
    title = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    country = models.CharField(max_length=25, default="")
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default="")
    category = models.ForeignKey(
        CategoryModel, related_name="products", on_delete=CASCADE
    )
    stripe_product_id = models.SlugField(max_length=100, default="")
    stripe_price_id = models.SlugField(max_length=100, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-date",)
