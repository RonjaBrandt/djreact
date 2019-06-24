from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('test/', views.Display.as_view(), name='test'),
    #Shows API for Survey
    path('surveyapi/', views.SurveyAPIView.as_view(), name='SurveyAPIView'),
    
    #path('list/', views.CategoryList.as_view(), name='list')
]
