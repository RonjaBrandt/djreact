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
    # Här är där jag håller på Eric.


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(2)
        try:
            # det är hit jag vill ha value, osäker på vilka värden som ska in på get_tooken här, den klagar om jag inte har 2 värden där
            qs = self.request.GET['response']
            print(qs)
            data = self.typeform_get('forms/{id}/responses?query={resp}'.format(id='g46uGI', resp=qs)).json()
            print(data)
            if Response.objects.get(response_id=qs):
                pass
            else:
                obj = Response.objects.create(response_id=qs)
                obj.save()

            typeform_API['items'] = data['items'] 
        except requests.HTTPError:
            pass
        else:
            # INte klart
            for item in data['items']:
                for answer in item['answers']:
                    try:
                        answer = Answer.objects.get(question=answer['field']['ref'])
                        response = Response.objects.get(response_id=qs)
                        if answer.question.category.category_Name == 'verksamhetsstyrning':
                            answer.answer == 
                        elif answer.question.category.category_Name == 'engagemang':
                            pass
                        elif answer.question.category.category_Name == 'resurser':
                            pass
                        elif answer.question.category.category_Name == 'resurser':
                            pass
                        question.category.current_Points += question.question_Points
                        question.category.save()
                    except Question.DoesNotExist:
                        pass

        context['questions'] = Question.objects.all()
        context['categorys'] = Category.objects.all()
        context['surveys'] = Survey.objects.all()
        #print(context)
        return context


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






