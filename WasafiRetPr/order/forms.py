from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'city', 'zip_code']
