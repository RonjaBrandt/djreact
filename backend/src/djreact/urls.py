from django.contrib import admin
from django.urls import path, include

# Handel url request, to the site.

urlpatterns = [
    path('admin/', admin.site.urls),

]
