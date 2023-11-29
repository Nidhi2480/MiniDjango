from django import forms
from .models import reviews
class laptopform(forms.ModelForm):
    class Meta:
        model=reviews
        fields=['name','specs','image']