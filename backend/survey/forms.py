from django import forms

from .models import Category

class CategoryModelForm(forms.ModelForm):
    current_Points = forms.DecimalField()

    class Meta:
       model = Category
       fields = [
            'current_Points',
        ]
    
    def __init__(self, *args, **kwargs):
        super(CategoryModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.required = False