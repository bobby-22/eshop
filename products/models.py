from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default="")
    description = models.TextField(default="")
    category = models.ForeignKey(CategoryModel, on_delete=CASCADE)
    stripe_product_id = models.CharField(blank=True, max_length=200, default="")
    stripe_price_id = models.CharField(blank=True, max_length=200, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(ProductModel, self).save(*args, **kwargs)
        thumbnail = Image.open(self.thumbnail.path)
        if thumbnail.width > 400 or thumbnail.height> 300:
            output_size = (400, 300)
            thumbnail.thumbnail(output_size)
            thumbnail.save(self.thumbnail.path)

    class Meta:
        verbose_name_plural = "Products"
