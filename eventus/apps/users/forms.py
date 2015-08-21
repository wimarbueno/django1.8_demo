from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre de usuario'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Ingrese un email'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Ingrese la contrasenia'}),
        }


class LoginForm(forms.Form):

    username = forms.CharField(max_length=30, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ingresa tu nombre usuario'}))
    password = forms.CharField(max_length=30, widget = forms.TextInput(attrs = {'type': 'password', 'class': 'form-control', 'placeholder': 'Escribe una contrasenia'}))
