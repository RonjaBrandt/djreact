from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('', views.index, name='index'),
    # /survey/<surveys_id>
    path('<int:surveys_id>/', views.detail, name='detail'),
    # /survey/<surveys_id>/results
    #re_path(r'(^?P<survey_id>[0-9]+)/results/$', views.results, name='results'),
    path('<int:surveys_id>/results/', views.results, name='results'),

]
