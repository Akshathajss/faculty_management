from django import forms
from .models import Faculty

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'CL', 'RH']
