from django.urls import path, include
from django.conf.urls import url
from . import views

# Handel url request, to the site.

urlpatterns = [
    # ex: /surveyResult/
    path('', views.index, name='index'),
]
