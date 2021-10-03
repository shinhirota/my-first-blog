from django import forms

from .models import Param

class ParamForm(forms.ModelForm):

    class Meta:
        model = Param
        fields = ('arg1', 'arg2',)
