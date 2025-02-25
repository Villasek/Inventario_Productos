from django import forms
from .models import producto




class ProductoForms(forms.Modelform):
    class meta:
        model = producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']