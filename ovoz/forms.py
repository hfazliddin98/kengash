from django import forms
from .models import Elon
from users.models import Davomat


class ElomForm(forms.ModelForm):
    class Meta:
        model = Elon
        fields = ['name', 'nomzod', 'rasm', 'vaqt']

class DavomatForm(forms.ModelForm):
    class Meta:
        model = Davomat
        fields = ['user', 'bor']