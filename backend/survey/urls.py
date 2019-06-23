from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('', views.IndexView.as_view(), name='index'),
    # /survey/<survey_id>
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/survey/add/
    path('survey/add/', views.SurveyCreate.as_view(), name='survey-add'),
    #/join/
    #path('join/', views.JoinFormView.as_view(), name='joinform'),

    path('test/', views.Display.as_view(), name='test'),
]