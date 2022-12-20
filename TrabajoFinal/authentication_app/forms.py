from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class AuthenticationForm(forms.Form):
    
    username = forms.CharField()
    password = forms.EmailField(label='Contraseña', widget=forms.PasswordInput)
    Mensaje = forms.CharField()

class UserRegisterForm(UserCreationForm):
    last_name= forms.CharField(label='Apellido')
    first_name= forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electronico')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ['username', 'email', 'last_name', 'first_name' 'password1', 'password2']

