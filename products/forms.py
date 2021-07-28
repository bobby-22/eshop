from django import forms
from django.db.models import fields
from .models import ProductModel

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["name", "price", "description"]
        labels = {"name": "Name", "description": "Description", "price": "Price"}
