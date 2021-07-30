from django.db import models

# Create your models here.
class ProductModel(models.Model):
    stripe_id = models.CharField(blank=True, max_length=200)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default="")

    def __str__(self):
        return "{} {} {} {}".format(self.stripe_id, self.name, self.description, self.price)
    
    class Meta:
        verbose_name_plural = "Product"