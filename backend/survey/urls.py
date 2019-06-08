from django.urls import path, re_path
from . import views

urlpatterns = [
    # /survey/
    path('', views.index, name='index'),

    # /survey/6214/  <-that is  (id)
    re_path(r'^(?P<survey_id>[0-9]+)/$', views.detail, name='detail'),
]
