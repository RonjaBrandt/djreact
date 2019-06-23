from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('', views.Display.as_view(), name='test'),
    path('test/', views.SurveyView.as_view(), name='SurveyView'),
    #Shows API for Survey
    path('surveys/', views.SurveyList.as_view()),
    #path('category/', views.CategoryList.as_view()),
    #path('index(', views.IndexView.as_view(), name='index'),
    # /survey/<survey_id>
    #path('index/<int:pk>/', views.DetailView.as_view(), name='detail'),    
]

urlpatterns = format_suffix_patterns(urlpatterns)