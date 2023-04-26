from django import forms

from app_main.models import videocard_directory_path

PARAMETER_CHOICES = [(1, 'Цена по возрастанию'), (2, 'Цена по убыванию')]
VIDEOCARD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
class FilterForm(forms.Form):
    parameter = forms.TypedChoiceField(required=False, choices=PARAMETER_CHOICES, coerce=int)
    search = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-input input-gray'}))

# class VideocardCreateForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     manufacturer = forms.CharField(max_length=20)
#     price = forms.IntegerField()
#     vendor = forms.CharField(max_length=50)
#     # promo_type = forms.CharField(max_length=10, choices=PROMO_TYPES_CHOICES, default='r')
#     image = forms.ImageField()
#     image_big = forms.ImageField()
#     info = forms.Form