from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('test/', views.Display.as_view(), name='test'),
    path('surveyapi/', views.SurveyAPIView.as_view(), name='SurveyAPIView'),
    #Shows API for Survey
    path('surveylist/', views.SurveyList.as_view(), name='surveylist'),
    path('questionlist/', views.QuestionList.as_view(), name='questionlist'),
   
    #path('category/', views.CategoryList.as_view()),
    #path('index(', views.IndexView.as_view(), name='index'),
    # /survey/<survey_id>
    #path('index/<int:pk>/', views.DetailView.as_view(), name='detail'),    
]

urlpatterns = format_suffix_patterns(urlpatterns)