from django import forms
from .models import ImageUploadModel
class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
# ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
# file = forms.FileField()
    image = forms.ImageField() 

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=ImageUploadModel
        fields=('description', 'document')
