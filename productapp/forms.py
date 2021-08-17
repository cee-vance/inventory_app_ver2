from django import forms

from productapp.models import Product

# a form for creating
# new products

class ProductForm(forms.ModelForm):

    class Meta: # data/ info configuration details for the class
        model = Product
        fields = ('name','description','price')
        

