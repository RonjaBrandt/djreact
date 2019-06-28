from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/test/
    path('test/', views.CategoryListView.as_view(), name='test'),
    #/survey/test/123
    path('test/<int:id>/', views.CategoryDetailView.as_view(), name='test-detail'),
    #/survey/test/update
    path('test/update/<int:pk>/', views.CategoryUpdate.as_view(), name='update'),
    #api
    path('test/chart/api/', views.ChartData.as_view(), name='api-chart'),
    path('test/question/api/', views.QuestionData.as_view(), name='api-Question')
]

urlpatterns = format_suffix_patterns(urlpatterns)