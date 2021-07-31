from django import forms
from django.db.models import fields
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ["stripe_product_id", "stripe_price_id"]
        labels = {"name": "Name", "description": "Description", "price": "Price"}