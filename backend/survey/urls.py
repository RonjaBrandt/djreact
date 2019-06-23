from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('', views.Display.as_view(), name='test'),
    path('index(', views.IndexView.as_view(), name='index'),
    # /survey/<survey_id>
    path('index/<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/survey/add/
    #path('survey/add/', views.QuestionCreate.as_view(), name='survey-add'),
    #/join/
    #path('join/', views.JoinFormView.as_view(), name='joinform'),

    
]