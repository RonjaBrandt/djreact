from django import forms

class Survey(forms.Form):
    url = forms.URLField()