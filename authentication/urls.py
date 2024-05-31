from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("saml/acs/", views.saml_acs, name="saml_acs"),
    path("mfa-verification/", views.mfa_verification, name="mfa_verification"),
]
