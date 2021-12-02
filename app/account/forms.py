from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django import forms
from django_registration.forms import RegistrationForm

from app.core.forms import BootsrapForm
from .models import Account


class AccountFormRegistration(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = Account


class AccountFormLogin(AuthenticationForm, BootsrapForm):
    """
        Кастомная форма авторизации
    """
    form_title = 'Вход в приложение'
