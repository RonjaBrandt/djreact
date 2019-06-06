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

    headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf',}
    response = requests.get('https://api.typeform.com/forms/nv4fXG/responses', headers=headers)
    print(response.json())


    return HttpResponse( 'Respons ID: ' + response.item_response_id + ' -Start Time: ' + response.item_landed_at + ' -End Time: ' + response.item_submitted_at + ' -HTTPadress/survey ID;: ' + response.item_metadata_referer + ' -NetworkID: ' + response.item_metadata_referer + 'Question ID: ' + response.answers_field_id + ' -Question Type: ' + response.answers_field_type + ' -Question Referens: ' + response.answers_field_ref + ' -Answer Type: ' + response.answers_type + ' -Choice: ' + response.answers + ' -end- ' )

        # print(response.json())
           # json = response.json()
           # serializer = SurveySerializer(data=json)
           # if serializer.is_valid():
           #     data = serializer.save()
              #  return 'Respons ID: ' + self.item_response_id + ' -Start Time: ' + self.item_landed_at + ' -End Time: ' + self.item_submitted_at + ' -HTTPadress/survey ID;: ' + self.item_metadata_referer + ' -NetworkID: ' + self.item_metadata_referer + 'Question ID: ' + self.answers_field_id + ' -Question Type: ' + self.answers_field_type + ' -Question Referens: ' + self.answers_field_ref + ' -Answer Type: ' + self.answers_type + ' -Choice: ' + self.answers + ' -end- '
   # else:
      #  form = Survey()



    #import requests
#
#
#headers = {
#    'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf',
#}
#
#response = requests.get('https://api.typeform.com/forms/nv4fXG/responses', headers=headers)

#print(response.json())