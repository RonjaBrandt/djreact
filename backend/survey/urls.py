from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'survey'

urlpatterns = [
    #generats tooken for the form and sends the user to Typeform
    path('start/', views._get_link , name='start'),
    # /survey/mdasmio1313JILAF
    path('<int:id>/', views.CategoryDetailView.as_view(), name='view'),
    #/survey/test/update
    path('test/update/<int:pk>/', views.CategoryUpdate.as_view(), name='update'),
    #api
    path('test/chart/api/', views.ChartData.as_view(), name='api-chart'),

    path('test/question/api/', views.QuestionData.as_view(), name='api-Question')
]

urlpatterns = format_suffix_patterns(urlpatterns)