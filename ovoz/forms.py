from django import forms
from .models import Taklif
from users.models import Davomat


class TaklifForm(forms.ModelForm):
    class Meta:
        model = Taklif
        fields = ['name', 'nomzod', 'vaqt']

class DavomatForm(forms.ModelForm):
    class Meta:
        model = Davomat
        fields = ['user_id', 'familya', 'ism']