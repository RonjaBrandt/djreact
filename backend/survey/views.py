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
    print(1)
    # Här är där jag håller på Eric.

    def get_context_data(self, **kwargs):
        print(2)
        try:
            qs = self.request.GET['response']
            print(qs)
            data = self.typeform_get('forms/{id}/responses?query={resp}'.format(id='g46uGI', resp=qs)).json()
            print(3)
            if Response.objects.filter(response_id=qs).exists():
                pass
            else:
                print(4)
                obj = Response.objects.create(response_id=qs)
                obj.save()
        except requests.HTTPError:
            pass
        try:
            typeform_API = data['items'][0]['answers']
            response = Response.objects.get(response_id=qs)
            survey = Survey.objects.all()
            category = Category.objects.all()
            question = Question.objects.all()
            answer = Answer.objects.all()
            response = Response.objects.all()
            #print(typeform_API[0]['field']) 
            #print(typeform_API[0]['field']['id'])
            # go throw all Categorys
            
            for category in category:
                    print('kategori')
                    print(category.category_Name)
                    print('question ID')
                    print(category.question_set.all())
                    # go throw all questions called fields from Typeform
                    for field in typeform_API:
                        print('Fråga')
                        print(field)
                        # If the category is this ->
                        if category.category_Name == 'verksamhetsstyrning':
                            print('hello från verksamhets')
                            print(question.question_Type)
                            # then check what if data category have a question with the same id as field
                            if question.question_ID == typeform_API[0]['field']['id']:
                                print('hej från question type')
                                # Then check what type that question have.
                                if question.question_Type == 'short_text'or'long_text'or'dropdown':
                                    print('hej från question type')
                                    # Then check if that answer is the same as the field answer is
                                    if
                                        # Finaly add points of that answer to
                                        # the Response field that have the same category name
                                elif question.question_Type == 'multiple_choice (multiple options)' or'picture_choice (single option)':
                                    pass

                                elif question.question_Type == 'multiple_choice (single option)' or'picture_choice (multiple options)':
                                    pass

                                elif question.question_Type == 'yes_no' and question.question_ID:
                                    pass
                                elif question.question_Type == 'rating':
                                    pass
                                elif question.question_Type == 'number':
                                    pass
                        # Else if the category is this ->
                        elif question.category.category_Name == 'engagemang':
                            if (question.question_Type == 'short_text'or'long_text'or'dropdown' and question.question_ID == typeform_API[0]['field']['id']):
                                print('hej från question type')
                            elif question.question_Type == 'multiple_choice (multiple options)' or'picture_choice (single option)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'multiple_choice (single option)' or'picture_choice (multiple options)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'yes_no' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'rating' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'number' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            pass

                        elif question.category.category_Name == 'kommunikation':
                            if (question.question_Type == 'short_text'or'long_text'or'dropdown' and question.question_ID == typeform_API[0]['field']['id']):
                                print('hej från question type')

                            elif question.question_Type == 'multiple_choice (multiple options)' or'picture_choice (single option)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'multiple_choice (single option)' or'picture_choice (multiple options)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'yes_no' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'rating' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'number' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            pass
                        elif question.category.category_Name == 'resurser':
                            if (question.question_Type == 'short_text'or'long_text'or'dropdown' and question.question_ID == typeform_API[0]['field']['id']):
                                print('hej från question type')

                            elif question.question_Type == 'multiple_choice (multiple options)' or'picture_choice (single option)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'multiple_choice (single option)' or'picture_choice (multiple options)' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'yes_no' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'rating' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            elif question.question_Type == 'number' and question.question_ID == typeform_API[0]['field']['id']:
                                pass
                            pass

        except Question.DoesNotExist:
            pass

      
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






