from django import http
from django.views import generic
from django.views.generic import FormView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from urllib.parse import urlparse

from random import choice
from string import ascii_letters, digits

from .models import Survey, Category, Question, Answer, Response
from .serializeres import SurveySerializer, CategorySerializer, QuestionSerializer
from .forms import CategoryModelForm
from .mixins import AjaxFormMixin

import json
import requests

#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.


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


# API view for catagory
class  ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

class  QuestionData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)

        return Response(serializer.data)



class TypeFormApiMixin:
    base_url="https://api.typeform.com/"
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
    print(1)
    #Check if objecet with the id exist or create a new one

    def get_queryset(self):
        return self.request.GET.get('')
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        print(2)
        print(self.get_queryset())
        try:
            data = self.typeform_get('forms/{id}/responses?query={resp}'.format(id='g46uGI', resp=self.get_queryset())).json()
            print(data)
            context['items'] = data['items'] #ev kan krångla se över. om ej kan kontakta api /admin view sen
        except requests.HTTPError:
            pass
        else:
            #Update scores here
            for item in data['items']:
                for answer in item['answers']:
                    try:
                        answer = Answer.objects.get(question_ID = answer['field']['ref'])
                        response= Response.objects.get(response_ID = answer['hidden']['query']) 
                        question.category.current_Points += question.question_Points
                        question.category.save()
                    except Question.DoesNotExist:
                        pass

        context['questions'] = Question.objects.all()
        context['categorys'] = Category.objects.all()
        context['surveys'] = Survey.objects.all()
        #print(context)
        return context

   
  

#Generat token for the form to send with to Typeforms hiddenfield 
def _generate_token(length=50):
    out = ""
    for i in range(length):
        out += choice(ascii_letters + digits)
    
    if Response.objects.filter(response_id = out) == True:
        _generate_token()
    else:
        pass
    return out

def _get_link(request):
    return redirect ("https://beyondintent.typeform.com/to/g46uGI?response_id=" + _generate_token())

'''
def create_object(self):
    print(3)
    obj = Response(response_id = get_id(), 
    verksamhetsstyrning = 0, 
    engagemang = 0, resurser= 0, 
    kommunikation= 0)
    obj.save()
    return redirect('survey:view')
  
'''




