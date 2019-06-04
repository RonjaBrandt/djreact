from django.urls import path, include
from . import views

# Handel url request, to the site.

urlpatterns = [
    # ex: /surveyResult/
    path('', views.index, name='index'),
]
