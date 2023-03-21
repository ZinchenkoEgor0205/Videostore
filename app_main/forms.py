from django import forms

PARAMETER_CHOICES = [(1, 'Цена по возрастанию'), (2, 'Цена по убыванию')]
VIDEOCARD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
class FilterForm(forms.Form):
    parameter = forms.TypedChoiceField(required=False, choices=PARAMETER_CHOICES, coerce=int)
    search = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={'class': 'form-input input-gray', 'placeholder': 'Поиск'}))