from django.contrib.auth import authenticate
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    '''
    Forms for product requiring:
    - name
    - description
    - owner
    '''
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'photo'
        ]

    def clean(self):
        msg = 'El nombre de producto ya existe, elige otro'
        cleaned_data = super(ProductForm, self).clean()
        try:
            product = Product.objects.get(name=cleaned_data['name'])
        except:
            if cleaned_data['price'] < 0:
                msg = 'El precio debe ser mayor a 0'
            else: 
                return self.cleaned_data
        raise forms.ValidationError(msg)
