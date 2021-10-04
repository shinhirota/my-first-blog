from django import forms
from .models import Dicom

class DicomForm(forms.ModelForm):
    class Meta:
        model = Dicom
        fields = ('description', 'file', )
