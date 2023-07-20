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

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Имя пользователя')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Пароль')}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_("Имя пользователя"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': _('Имя пользователя')}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': _('Пароль')}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Повторите пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': _('Повторите пароль')}),
        strip=False,
        help_text=_("Повторите ранее написанный пароль для верификации."),
    )
    first_name = forms.CharField(max_length=30, required=False, help_text='Name', widget=forms.TextInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Имя')}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name', widget=forms.TextInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Фамилия')}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Email')}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Город')}))
    phone = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-input input-gray', 'placeholder': _('Телефон')}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        field_classes = {"username": UsernameField}


class AccountEditForm(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Имя пользователя')}))
    first_name = forms.CharField(required=False, max_length=30, help_text='Name',
                                 widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Имя')}))
    last_name = forms.CharField(required=False, max_length=30, help_text='Last name',
                                widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Фамилия')}))
    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': _('Email')}))
    city = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Город')}))
    phone = forms.CharField(required=False,
                            widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': _('Телефон')}))
    street = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Улица')}))
    housing = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Корпус')}))
    house = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Дом')}))
    apartment = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Квартира')}))