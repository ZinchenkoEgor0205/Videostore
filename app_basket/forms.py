from django import forms

VIDEOCARD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BasketAddVideocardForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=VIDEOCARD_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.Form):
    name_surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия и имя'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Телефон'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    city = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}))
    street = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Улица'}))
    house = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Дом'}))
    housing = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Корпус'}))
    apartment = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Квартира'}))