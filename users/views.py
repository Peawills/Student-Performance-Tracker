from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm  # custom form that extends UserCreationForm


# Home View
def home_view(request):
    return render(request, "users/home.html")


# Signup View
def signup_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # If you added a role field in your custom User model, set default role
            if not user.role:
                user.role = "student"
            user.save()
            login(request, user)  # automatically log them in after signup
            return redirect("dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")


# Dashboard (protected page after login)
@login_required
def dashboard_view(request):
    return render(request, "users/dashboard.html", {"user": request.user})
