from django.contrib.auth.views import LoginView
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from .forms import AccountFormRegistration, AccountFormLogin

urlpatterns = [
    path('register/',
         RegistrationView.as_view(
             form_class=AccountFormRegistration,
             template_name='registration/registration_form.html'
         ),
         name='django_registration_register',
         ),
    path('', include('django_registration.backends.one_step.urls')),

    path('login/', LoginView.as_view(
        form_class=AccountFormLogin,
        template_name='registration/login_form.html'
    ), name='login'),
    path('', include('django.contrib.auth.urls')),

]