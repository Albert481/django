from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth import (authenticate, get_user_model, login, logout, update_session_auth_hash)
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from accounts import EditProfile, LoginForm, RegisterForm
from accounts.models import Profile

def login_view(request):
    form = LoginForm.UserLoginForm(request.POST or None)
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            print('Login Validated')
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                print('Successfully Logged In')
                return redirect('profile')
            else:
                print('User invalid')
    context = {
        "form": form,
    }

    return render(request, "login.html", context)

def register_view(request):
    form = RegisterForm.UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #Authenticates user before logging in
            # new_user = authenticate(username=user.username, password=password)
            # login(request, new_user)

            #Set default values to accounts_profile
            new_entry = Profile(email=user, ethaddress='null', indicativecontribution=0, actualcontribution=0, mytoken=0, bonustoken=0, tokenwithdrawn=0)
            new_entry.save()
            print('Successfully registered')
            return redirect('../')

    context = {
        "form": form,
    }

    return render(request, "register.html", context)

def profile_view(request):
    #Retrieves all data from accounts.profile
    data = Profile.objects.all()
    current_user = request.user
    form = EditProfile.EditValues(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            entry = form.save(commit=False)
            ethaddress = form.cleaned_data['ethaddress']
            indicativecontribution = form.cleaned_data['indicativecontribution']
            entry = Profile(email=current_user, ethaddress=ethaddress, indicativecontribution=indicativecontribution)
            entry.save()


    context = {
        "data": data,
        "form": form
    }

    return render(request, "profile.html", context)

def password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')