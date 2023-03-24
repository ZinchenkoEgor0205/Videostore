from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].localize = True
        self.fields['username'].widget.is_localized = True

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Name', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}))
    phone = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Телефон'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        field_classes = {"username": UsernameField}


class AccountEditForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
    first_name = forms.CharField(required=False, max_length=30, help_text='Name',
                                 widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}))
    last_name = forms.CharField(required=False, max_length=30, help_text='Last name',
                                widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    city = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}))
    phone = forms.CharField(required=False,
                            widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Телефон'}))
    street = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Улица'}))
    housing = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Корпус'}))
    house = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Дом'}))
    apartment = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Квартира'}))