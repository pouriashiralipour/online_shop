from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        field = ['first_name', 'last_name', 'phone_number', 'address', 'order_note']
