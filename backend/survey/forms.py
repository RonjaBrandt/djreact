from django import forms

from .models import Category, Answer

class CategoryModelForm(forms.ModelForm):

    class Meta:
       model = Category
       fields = [
            'current_Points',
        ]
