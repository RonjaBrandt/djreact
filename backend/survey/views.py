from django import http
from django.views import generic
from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from urllib.parse import urlparse, parse_qs

from random import choice
from string import ascii_letters, digits

from .models import Survey, Category, Question, Answer, Response
from .serializeres import SurveySerializer, CategorySerializer, QuestionSerializer
from .forms import CategoryModelForm
from .mixins import AjaxFormMixin

import json
import urllib.request
import urllib.parse as urlparse
import requests

class TypeFormApiMixin:
    base_url ="https://api.typeform.com/"
    headers = {'Authorization': 'Bearer G5YQ7E5yn8qRdVMcAEUxEHpvHNjnnhq8EUXsrChdqid7'}

    def _get_url(self, path):
        return self.base_url + path

    def typeform_get(self, path):
        r = requests.get(self._get_url(path), headers=self.headers)
        r.raise_for_status()
        return r


# List
class ResponseListView(ListView, TypeFormApiMixin):
    model = Response
    template_name = 'survey/index.html'

    # Här är där jag håller på Eric.

    def get_context_data(self, **kwargs):

        try:
            qs = self.request.GET['response']
            print(qs)
            data = self.typeform_get('forms/{id}/responses?query={resp}'.format(id='g46uGI', resp=qs)).json()

            if Response.objects.filter(response_id=qs).exists():
                pass
            else:

                obj = Response.objects.create(response_id=qs)
                obj.save()
        except requests.HTTPError:
            pass
       
        typeform_API = data['items'][0]['answers']
        response = Response.objects.get(response_id=qs)
        survey = Survey.objects.all()
        #category = Category.objects.all()
        #question = Question.objects.all()
        #answer = Answer.objects.all()
        response = Response.objects.all()
        typeform_ID = {}
        
        
        for field in typeform_API:
         #   print(field.get('boolean', ''))
          #  print(field.get('text', ''))
         # try:
           #   print(field["boolean"])
        #  except:
         #     pass
              
            
            #typeform_ID = field['field']['ref']
            #print(typeform_ID)
    #        try:
    #            obj = Question.objects.get(question_ID= field['field']['ref'])
    #            print('Fungerar')
     #           print(obj.question_Type)
      #          if obj.question_Type == 'boolan':
   #                 print('typen här')
     #               print(obj)
        #            print(field['type'])
    #                print(field['field']['ref'])
   #                 boolan_answer = Answer.objects.get(answer=field['field']['ref'])
    #                print(boolan_answer)
                               
    #        except Question.DoesNotExist:
     #           print('fungerar inte')
     #           print(field['field']['ref'])
      #      else:
      #          pass
                
            #print(question_ref)

      

      
        #print(context)
        #return context


# Generat token for the form to send with to Typeforms hiddenfield
def _generate_token(length=50):
    out = ""
    for i in range(length):
        out += choice(ascii_letters + digits)
    if Response.objects.filter(response_id=out) is True:
        _generate_token()
    else:
        pass
    return out


def _get_link(request):
    return redirect("https://beyondintent.typeform.com/to/g46uGI?response_id=" + _generate_token())


def create_object(self):
    return redirect('survey:view')






