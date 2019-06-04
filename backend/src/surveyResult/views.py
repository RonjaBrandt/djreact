from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Sendsback the respons.
    return HttpResponse("This is the result homepage")