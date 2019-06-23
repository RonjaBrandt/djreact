from django.contrib import admin
from .models import Question, Category, Survey

admin.site.register(Survey)
admin.site.register(Category)
admin.site.register(Question)


