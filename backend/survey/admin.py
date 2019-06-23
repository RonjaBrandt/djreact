from django.contrib import admin
from .models import Question, Score, Survey

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Score)


