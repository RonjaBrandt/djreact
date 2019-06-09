from django.urls import path, re_path
from . import views

urlpatterns = [
    # /survey/
    path('', views.index, name='index'),
    # /survey/<surveys_id>
    path('<int:surveys_id>/', views.detail, name='detail'),
]
