from django.contrib import admin
from django.urls import path, include



# Handel url request, to the site.

urlpatterns = [
    # ex: /admin/
    path('admin/', admin.site.urls),
    # ex: /surveyresult/
    path('surveyresult/', include('surveyResult.urls')),

    
]
