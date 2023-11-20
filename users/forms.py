from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Foydalanuvchi')
    password = forms.CharField(label='Parol')


class RoyhatForm(forms.ModelForm):    
    username = forms.CharField(label='Foydalanuvchi')
    first_name = forms.CharField(label='Ism')
    last_name = forms.CharField(label='Familya')
    lavozim = forms.SelectMultiple()
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Parolni takrorlang', widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'lavozim', 'password']
        # fields = ('__all__')

    def claen_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Ikkala parol bir biriga teng emas !!!')
        
        return data['password2']

    