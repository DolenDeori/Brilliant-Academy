from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm

def Registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = request.POST["email"]
            password = request.POST["password1"]
            user = authenticate(email = email, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)

                return redirect("/")
    else:
        form = AccountAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("home")

