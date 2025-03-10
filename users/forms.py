from django import forms
from django.contrib.auth.forms import UserCreationForm # UserCreationForm is a built-in form for creating a new user wwhich compares passwword1 and password2
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm): 

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    

class LoginForm(forms.Form):
    email_or_username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)
    