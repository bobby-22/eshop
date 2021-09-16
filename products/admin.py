from django.contrib import admin
from .models import ProductModel, ImageModel, ReviewModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(ImageModel)
admin.site.register(ReviewModel)
