from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

# Handel url request, to the site.

urlpatterns = [
    # /surveyResult/
    path('', views.save_survey, name='survey'),
    #path('survey/', views.save_survey, name='survey'),
    # /surveyResult/123  (id)
    re_path(r'^(?P<survey_id>[0-9]+)/$', views.detail, name='detail'),
]
