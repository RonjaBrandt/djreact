from django.urls import path
from . import views

urlpatterns = [
    # /survey/
    path('', views.index, name='index'),

    # /survey/6214/
    path(r'^(?P<survey_id>[')
]
