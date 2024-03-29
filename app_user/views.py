from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from app_user.forms import AuthForm, RegisterForm, AccountEditForm
from app_user.models import Profile
from django.urls import reverse, reverse_lazy


class LoginView(View):

    def get(self, request):
        form = AuthForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):

        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                message = _('Неверно введён логин или пароль')
                context = {
                    'form': form,
                    'message': message,
                }
                return render(request, 'login.html', context=context)
            if user and user.is_active:
                login(request, user)
                return redirect(reverse('main_view'))
            else:
                return render(request, 'login.html')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.errors:
            errors = []
            for value in form.errors:
                [errors.append(data.args[0]) for data in form.errors[value].data]
            return render(request, 'register.html', {'form': form, 'errors': errors})
        elif form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone,
                discount_id=4,
                total_sum=0,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')


class AccountView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'account.html', context=context)


class AccountEditView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def get(self, request):
        user = request.user
        form = AccountEditForm()
        return render(request, 'account-edit.html', {'form': form, 'user': user})

    def post(self, request):
        user = request.user
        form = AccountEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user.username = cd['username']
            user.email = cd['email']
            user.profile.phone = cd['phone']
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.profile.city = cd['city']
            user.profile.street = cd['street']
            user.profile.housing = cd['housing']
            user.profile.house = cd['house']
            user.profile.apartment = cd['apartment']
            user.save()
            user.profile.save()
            return redirect(reverse('account'))


def logout_view(request):
    logout(request)
    redirect('/')