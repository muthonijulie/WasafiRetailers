from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    shipping_name = forms.CharField(max_length=255, label="Full Name")
    shipping_email = forms.EmailField(label="Email")
    phone_number = forms.CharField(max_length=20, label="Phone Number")
    shipping_address = forms.CharField(widget=forms.Textarea, label="Address")
    shipping_city = forms.CharField(max_length=100, label="City")
    shipping_zip_code = forms.CharField(max_length=20, label="Zip Code")

    class Meta:
        model = Order
        fields = ['shipping_name', 'shipping_email', 'phone_number', 'shipping_address', 'shipping_city', 'shipping_zip_code']
