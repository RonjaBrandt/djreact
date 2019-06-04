from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Sendsback the respons.
    return HttpResponse("This is the result homepage")

def detail(request, survey_id):
    return HttpResponse("Details for the Answers with id: " + str(survey_id) + ".")