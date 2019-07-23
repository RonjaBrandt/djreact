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
    base_url = "https://api.typeform.com/"
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
       # response = Response.objects.all()
        categorys = Category.objects.all()
        questions = Question.objects.all()
        answers = Answer.objects.all()
        for field in typeform_API:
            try:
                # field[] is a dict
                # obj is a object of class Question
                # Checks if there is a Question in the DB with the ref from Tyoe form
                if Question.objects.get(question_ID=field['field']['ref']):
                    obj = Question.objects.get(question_ID=field['field']['ref'])
                  #  print(field)
                    # 'choice', 'choices',
                    for bool_answer in answers.filter(bool_answer=field['boolean']):
                        _id = bool_answer.id
                        b1 = answers.get(pk=_id)

                        #point = b1.points
                        #for category in categorys:

                        if str(obj.category) == 'verksamhetsstyrning':
                            print(obj)
                            print(obj.category)
                            response.verksamhetsstyrning += b1.points
                            response.save()
                            break
                        elif str(obj.category) == 'engagemang':
                            print(obj)
                            print(obj.category)
                            response.engagemang += b1.points
                            response.save()
                            break
                        elif str(obj.category) == 'kommunikation':
                            print(obj)
                            print(obj.category)
                            response.kommunikation += b1.points
                            response.save()
                            break
                        elif str(obj.category) == 'resurser':
                            print(obj)
                            print(obj.category)
                            response.resurser += b1.points
                            response.save()
                            break

                elif Question.objects.get(question_ID=field['field']['ref']):
                    obj = Question.objects.get(question_ID=field['field']['ref'])
                  #  print(field)
                    # 'choice', 'choices',
                    for chocie_answer in answers.filter(the_answer=field['choice']):
                        _id = chocie_answer.id
                        b1 = answers.get(pk=_id)

                        #point = b1.points
                        #for category in categorys:

                        if str(obj.category) == 'verksamhetsstyrning':
                            #print(b1.points)
                            response.verksamhetsstyrning += b1.points
                            response.save()
                        elif str(obj.category) == 'engagemang':
                            response.engagemang += b1.points
                            response.save()
                        elif str(obj.category) == 'kommunikation':
                            response.kommunikation += b1.points
                            response.save()
                        elif str(obj.category) == 'resurser':
                            response.resurser += b1.points
                            response.save()        

                elif Question.objects.get(question_ID=field['field']['ref']):
                    obj = Question.objects.get(question_ID=field['field']['ref'])
                  #  print(field)
                    # 'choice', 'choices',
                    for chocies_answer in answers.filter(the_answer=field['choices']):
                        _id = chocies_answer.id
                        b1 = answers.get(pk=_id)

                        #point = b1.points
                        #for category in categorys:

                        if str(obj.category) == 'verksamhetsstyrning':
                            #print(b1.points)
                            response.verksamhetsstyrning += b1.points
                            response.save()
                        elif str(obj.category) == 'engagemang':
                            response.engagemang += b1.points
                            response.save()
                        elif str(obj.category) == 'kommunikation':
                            response.kommunikation += b1.points
                            response.save()
                        elif str(obj.category) == 'resurser':
                            response.resurser += b1.points
                            response.save()        
            except:
                pass


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






