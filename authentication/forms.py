from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)


class MFAVerificationForm(forms.Form):
    token = forms.CharField(max_length=6, help_text="Enter the 6-digit MFA token")
