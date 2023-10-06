from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль:')
    username = forms.CharField(help_text="", label='Имя пользователя:')

    class Meta:
        model = User
        fields = ['username', 'password']
