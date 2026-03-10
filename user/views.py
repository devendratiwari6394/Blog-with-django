from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

User = get_user_model()


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        if password != re_password:
            messages.error(request, "Passwords do not match")
            return redirect("registration")

        if User.objects.filter(email=email).exists():
            messages.error(request, "User already exists")
            return redirect("registration")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "user/register.html")


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)

            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("home")

        messages.error(request, "Invalid email or password")
        return redirect("login")

    return render(request, "user/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")