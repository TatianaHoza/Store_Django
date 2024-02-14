from django import forms
from .models import ProductModel

class ProductImage(forms.Form):
    class Meta:
        model = ProductModel
        fields = ['name', 'image']


