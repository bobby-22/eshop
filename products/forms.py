from django import forms
from django.db.models import fields
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ["stripe_id"]
        labels = {"name": "Name", "description": "Description", "price": "Price"}