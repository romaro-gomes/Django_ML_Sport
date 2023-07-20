from django import forms
from . import models

class DataForm(forms.ModelForm):
    class Meta:
        model=models.Data
        fields= ['name','age','height','sex']