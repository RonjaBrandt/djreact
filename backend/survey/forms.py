from django import forms
from django.db import models
from .models import Category

class CategoryModelForm(forms.ModelForm):
    current_Points = models.DecimalField()

    class Meta:
        model = Category
        fields = [
            'current_Points',
        ]