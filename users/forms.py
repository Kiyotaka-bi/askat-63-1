from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Электронная почта")
    first_name = forms.CharField(max_length=30, label="Имя")
    last_name = forms.CharField(max_length=30, label="Фамилия")
    phone = forms.CharField(max_length=20, label="Номер телефона")
    city = forms.CharField(max_length=100, label="Город")
    birth_date = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    bio = forms.CharField(label="О себе", widget=forms.Textarea(attrs={'rows': 3}))
    favorite_genre = forms.CharField(max_length=100, label="Любимый жанр")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'email', 'first_name', 'last_name', 'phone', 'city', 'birth_date', 'bio', 'favorite_genre'
        )

class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField(label="Введите код с картинки")