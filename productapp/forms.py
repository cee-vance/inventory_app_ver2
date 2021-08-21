from django import forms

from productapp.models import Product, ProductCategory

# a form for creating
# new products

class ProductForm(forms.ModelForm):

    class Meta: # data/ info configuration details for the class
        model = Product
        fields = ('name','description','price')
        

class ProductCategoryForm(forms.ModelForm):
    """
    form for creating a productCategory

    """
    class Meta:
        model = ProductCategory
        fields = '__all__'