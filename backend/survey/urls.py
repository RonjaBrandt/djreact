from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/test/
    path('test/', views.CategoryListView.as_view(), name='test'),
    #/survey/test/123
    path('test/<int:id>/', views.CategoryDetailView.as_view(), name='test-detail'),

    #Shows API for Survey
    path('surveyapi/', views.SurveyAPIView.as_view(), name='SurveyAPIView'),
    #/survey/test/update
    path('test/update/<int:pk>/', views.CategoryUpdate.as_view(), name='update')
    
    #path('list/', views.CategoryList.as_view(), name='list')
]
