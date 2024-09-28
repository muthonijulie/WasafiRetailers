from django import forms
from .models import Product,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
      
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','price','stock','category','image','is_active']