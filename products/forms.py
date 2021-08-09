from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["name", "description", "price"]
        labels = {"name": "Name", "description": "Description", "price": "Price"}