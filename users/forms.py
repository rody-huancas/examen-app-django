from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import usuario


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"placeholder": "Inicio de sesión"}),
    )
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = usuario
        fields = ["username", "full_name", "email", 'telefono',"password1", "password2"]
