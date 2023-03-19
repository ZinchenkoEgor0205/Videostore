from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app_user.forms import AuthForm, RegisterForm, AccountEditForm
from app_user.models import Profile
from videostore_project.settings import BASE_DIR


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('/')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'login.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def account_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'account.html', context=context)

def account_edit_view(request):
    user = request.user
    if request.method == 'POST':
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
            return redirect('/user/account')
    else:
        form = AccountEditForm()
    return  render(request, 'account-edit.html', {'form': form, 'user': user})

def logout_view(request):
    logout(request)
    redirect('/')