from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
class UserRegister(View):
    def get(self, request):
        form = UserRegisterForm
        context = {"form": form}
        return render(request, "accounts/register.html", context)
    
    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        context = {"form": form}
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password2 = form.cleaned_data.get("password2")
            User.objects.create_user(username, email, password2)
            new_user = authenticate(username=username, password=password2)
            if new_user is not None:
                login(request, new_user)
                return redirect("products:index")
            else:
                messages.info(request, "Incorrect username or password")
                return redirect("accounts:user_login")
        else:
            return render(request, "accounts/register.html", context)


class UserLogin(View):
    def get(self, request):
        form = UserLoginForm
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("products:index")
            else:
                messages.info(request, "Incorrect username or password")
                return redirect("accounts:user_login")

def user_logout(request):
    logout(request)
    return redirect("products:index")
