from django.views import generic
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Surveys
from .forms import JoinForm
#from .mixins import AjaxFormMixin,
from .mixins import JsonFormMixin
import json


#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.##

'''
class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name  = 'forms/ajax.html'
    success_url = '/form-success/'
'''

class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'all_surveys'        

    def get_queryset(self):
        return Surveys.objects.all()


class DetailView(generic.DetailView):
    model = Surveys
    template_name='survey/detail.html'

# TROLIGEN ÄR DET HÄR SOM JSON DATA SKA IN PÅ NÅGOT SÄTT
class SurveyCreate(JsonFormMixin, CreateView):
    model = Surveys
    fields = ['titlel', 'items']