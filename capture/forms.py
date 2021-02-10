from django import forms
from .models import ImageUploadModel

class UploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField() 

class DetectForm(forms.ModelForm):
    class Meta:
        model=ImageUploadModel
        fields=('description', 'document')
