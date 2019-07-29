from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'survey'

urlpatterns = [
    # generats tooken for the form and sends the user to Typeform
    path('start/', views._get_link, name='start'),

    # /survey/mdasmio1313JILAF
    path('response_id/', views.ResponseListView.as_view(), name='view'),

    path('response_id/?response=<value>', views.create_object, name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
