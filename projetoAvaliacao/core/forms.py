from django import forms
from .models import faculdade

class TaskForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    professor = forms.CharField(max_length=100)
    
    
    class Meta:
        model = faculdade
        fields = ['nome', 'professor']