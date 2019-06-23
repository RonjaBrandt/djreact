from django.views import generic
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Survey
import json
import requests


#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.

class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'all_survey'        

    def get_queryset(self):
        return Survey.objects.all()


class DetailView(generic.DetailView):
    model = Survey
    template_name='survey/detail.html'


# Sedan se över Cash ramverket. Django Cash
class SurveyCreate(CreateView):
    model = Survey
    fields = ['titlel', 'items']

    
class Display(generic.TemplateView):
    #Getting the hole form (forms)
    template_name = 'survey/index.html'
    #URL to get the latest repsonses
    url="https://api.typeform.com/forms/nv4fXG/responses?page_size=1"
    headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Felhantera sen
        r = requests.get(self.url, headers=self.headers)
        #Felhantera sen try exept
        json = r.json()
        #Dictionary / Key, felhantera sen.
        context['items'] = json['items']

        return context
    
 