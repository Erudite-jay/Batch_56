from django import forms
from .models import FileUpload

#normal forms
# class FileUploadFormClass(forms.Form):
#     name=forms.CharField(max_length=100)
#     file=forms.FileField()

#model forms
class FileUploadFormClass(forms.ModelForm):
    class Meta:
        model=FileUpload
        fields='__all__'