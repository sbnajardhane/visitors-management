from django import forms
from .models import Data


class uploadExcel(forms.ModelForm):

    class Meta:
        model = Data
        fields = ['file_name']