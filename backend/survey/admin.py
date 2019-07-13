from django.contrib import admin
from .models import Question, Category, Survey, Answer, Response

admin.site.register(Survey)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Response)


