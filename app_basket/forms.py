from django import forms

VIDEOCARD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BasketAddVideocardForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=VIDEOCARD_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)