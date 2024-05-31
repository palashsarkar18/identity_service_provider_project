from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import LoginForm, MFAVerificationForm
from .models import MFAToken
from .saml import initiate_saml_login, process_saml_response
from .mfa import send_mfa_token, verify_mfa_token


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return initiate_saml_login(request, user)
    else:
        form = LoginForm()
    return render(request, "authentication/login.html", {"form": form})


def saml_acs(request):
    user = process_saml_response(request)
    if user:
        send_mfa_token(user)
        return redirect("mfa_verification")
    return redirect("login")


@login_required
def mfa_verification(request):
    if request.method == "POST":
        form = MFAVerificationForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data["token"]
            if verify_mfa_token(request.user, token):
                return redirect("home")
    else:
        form = MFAVerificationForm()
    return render(request, "authentication/mfa_verification.html", {"form": form})
