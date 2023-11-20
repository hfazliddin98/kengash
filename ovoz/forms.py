from django import forms
from .models import Elon


class ElomForm(forms.ModelForm):

    class Meta:
        model = Elon
        fields = ['name', 'nomzod', 'rasm', 'vaqt']