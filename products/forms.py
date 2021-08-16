from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ["name", "description", "thumbnail", "image", "price", "category"]
        