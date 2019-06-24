from django.views import generic
from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Survey, Category, Question
from .serializeres import SurveySerializer, CategorySerializer, QuestionSerializer
from .forms import CategoryModelForm

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
        context['question'] = Question.objects.all()
        context['category'] = Category.objects.all()
       
        return context
    
    def post(self, requests):
        form = CategoryModelForm(requests.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['current_Points']
            form = CategoryModelForm()
            return redirect('survey:test')
        
        args ={'form': form, 'text': text}
        return render(request, self.template_name, args)
