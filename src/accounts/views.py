from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from blog.local_settings import DEFAULT_FROM_EMAIL

from .forms import UserLoginForm, UserRegisterForm

User = get_user_model()

def login_view(request):
    title = "Login"
    login_page = True
    next_page = request.GET.get("next")
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if next_page:
                return redirect(next_page)
            return redirect("/")
        else:
            messages.error(request, "Incorrect username and/or password.")

    context = {
        "title": title,
        "form": form,
        "login_page": login_page
    }
    return render(request, "form.html", context)

def register_view(request):
    title = "Register"
    login_page = False
    next_page = request.GET.get("next")
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()

        subject = "New Registered User!"
        message = "A new user has been registered by the username of " + user.username + "."
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL], fail_silently=True)

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    context = {
        "title": title,
        "form": form,
        "login_page": login_page
    }
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")
