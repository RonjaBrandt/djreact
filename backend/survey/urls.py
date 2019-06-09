from django.urls import path, re_path
from . import views

app_name = 'survey'

urlpatterns = [
    # /survey/
    path('', views.IndexView.as_view(), name='index'),
    # /survey/<surveys_id>
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
