from django.views import generic
from django.views.generic import FormView, TemplateView, ListView, DetailView


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Survey, Category, Question
from .serializeres import SurveySerializer, CategorySerializer, QuestionSerializer
from .forms import SurveyForm

import json
import requests
#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.

#Make data on the database to APIrepsonse

class SurveyAPIView(APIView):

    def get(self, request):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)


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

     

class SurveyList(ListView):
    template_name = 'survey/index.html'
    model = Survey
    context_object_name ='survey'


class QuestionList(ListView):
    template_name = 'survey/index.html'
    model = Question
    context_object_name ='question'