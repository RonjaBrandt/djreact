from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import requests

from .forms import  Survey
from .serializer import SurveySerializer


def index(request):
    #Sendsback the respons.
    return HttpResponse("This is the result homepage")

def detail(request, survey_id):
    return HttpResponse("Details for the Answers with id: " + str(survey_id) + ".")




def save_survey(request):
   headers = {
    'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf',
}
   response = requests.get('https://api.typeform.com/forms/nv4fXG/responses', headers=headers)

   print(response.json())

   return HttpResponse("se if get respons in consol" + str(response.json()))