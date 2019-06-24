from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('test/', views.Display.as_view(), name='test'),
    #Shows API for Survey
    path('surveyapi/', views.SurveyAPIView.as_view(), name='SurveyAPIView'),
    
    #path('surveylist/', views.SurveyList.as_view(), name='surveylist'),
    path('questionlist/', views.QuestionList.as_view(), name='questionlist'),
   
    #path('category/', views.CategoryList.as_view()),
    #path('index(', views.IndexView.as_view(), name='index'),
    # /survey/<survey_id>
    #path('index/<int:pk>/', views.DetailView.as_view(), name='detail'),    
]
