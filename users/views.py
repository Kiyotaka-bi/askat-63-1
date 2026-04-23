from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomRegisterForm, LoginFormWithCaptcha


class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class MyLoginView(LoginView):
    form_class = LoginFormWithCaptcha
    template_name = 'users/login.html'
    redirect_authenticated_user = True  

    def get_success_url(self):
        return reverse_lazy('home')  