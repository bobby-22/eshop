from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default="")
    stripe_product_id = models.CharField(blank=True, max_length=200, default="")
    stripe_price_id = models.CharField(blank=True, max_length=200, default="")

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.description, self.price, self.stripe_product_id, self.stripe_price_id)
    
    class Meta:
        verbose_name_plural = "Product"