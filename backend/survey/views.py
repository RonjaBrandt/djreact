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
        response = Response.objects.all()

        for field in typeform_API:
            try:
                #field[] is a dict
                #obj is a object of class Question
                obj = Question.objects.get(question_ID=field['field']['ref'])
                
                # This get all the answers who are of type boolean.
                boolan_answers = field['boolean']
                b1 = Answer.objects.all().filter(the_answer=boolan_answers).values()
                print(list(b1.keys()))
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






