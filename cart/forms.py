from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int, label=_('quantity'))
