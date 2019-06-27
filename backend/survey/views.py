from django import http
from django.views import generic
from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from random import choice
from string import ascii_letters, digits

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

class CategoryUpdate(AjaxFormMixin ,UpdateView):
    model = Category
    fields = ['current_Points']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return http.JsonResponse({'status': 'SUCCESS', 'value': self.object.current_Points})




class TypeFormApiMixin:
    base_url="https://api.typeform.com/"
    headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf'}

    def _get_url(self, path):
        return self.base_url + path

    def typeform_get(self, path):
        r = requests.get(self._get_url(path), headers=self.headers)
        r.raise_for_status()
        return r
        

        

#generic.TemplateView
class CategoryListView(ListView, TypeFormApiMixin):
    #Getting the hole form (forms)
    model = Category
    template_name = 'survey/index.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            data = self.typeform_get('forms/{id}/responses?page_size=1'.format(id='nv4fXG')).json()
            context['items'] = data['items'] #ev kan krångla se över. om ej kan kontakta api /admin view sen
        except requests.HTTPError:
            pass

        context['questions'] = Question.objects.all()
        context['categorys'] = Category.objects.all()
        context['surveys'] = Survey.objects.all()
        print(context)
        return context

#generic.TemplateView
#Detailview 
class CategoryDetailView(DetailView, TypeFormApiMixin):
    #Getting the hole form (forms)
    model = Category
    template_name = 'survey/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Felhantera sen
        try:
            data = self.typeform_get('forms/{id}/responses?page_size=1'.format(id='nv4fXG'))
            context['items'] = data['items']
        except requests.HTTPError:
            pass
        
        context['questions'] = Question.objects.all()
        context['categorys'] = Category.objects.all()
        context['surveys'] = Survey.objects.all()
        print(context)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Category, id=id_)



#Generat token for the form to send with to Typeforms hiddenfield 

def _generate_token(length=50):
   out = ""
   for i in range(length):
       out += choice(ascii_letters + digits)
   return out


def _get_link():
   return "http://someserver.somewhere?token=" + _generate_token()