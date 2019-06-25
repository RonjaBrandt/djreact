from django import http
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
from .mixins import AjaxFormMixin

import json
import requests
#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.

#Make data on the database to APIrepsonse
class SurveyAPIView(APIView):

    def get(self, request):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)

class JoinFormView(AjaxFormMixin, FormView):
    form_class = CategoryModelForm
    template_name = 'survey/index.html'

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['current_Points']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return http.JsonResponse({'status': 'SUCCESS', 'value': 1})

#generic.TemplateView
class CategoryListView(ListView):
    #Getting the hole form (forms)
    model = Category
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
        print(context)
        context['category'] = Category.objects.all()
        
       
        return context

#generic.TemplateView
#Detailview 
class CategoryDetailView(DetailView):
    #Getting the hole form (forms)
    model = Category
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
        
        print(context)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Category, id=id_)
