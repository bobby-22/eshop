from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name, self.description, self.price
    
    class Meta:
        verbose_name_plural = "Product"