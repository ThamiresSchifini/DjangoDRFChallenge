from django import forms

class UploadFileTextForm(forms.Form):
    file = forms.FileField()