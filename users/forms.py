from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Foydalanuvchi')
    password = forms.CharField(label='Parol')



    