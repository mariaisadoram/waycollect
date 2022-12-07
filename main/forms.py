from django import forms
from main.models import Local

class LocalForm(forms.ModelForm):
    class Meta:
        model=Local
        fields='__all__'
