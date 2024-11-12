from django import forms


class PaymentForm(forms.Form):
    phone_number = forms.CharField(label="Phone number", max_length=15)
    amount = forms.IntegerField(label="Amount", min_value=1)