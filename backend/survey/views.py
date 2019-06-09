from django.http import Http404
from django.shortcuts import render
from .models import Surveys

def index(request):
    all_surveys = Surveys.objects.all()
    context = {'all_surveys': all_surveys} 
    return render(request, 'survey/index.html', context)

def detail(request, surveys_id):
    try:
        surveys = Surveys.objects.get(pk=surveys_id)
    except Surveys.DoesNotExist:
        raise Http404("Survey does not exist")
    return render(request, 'survey/detail.html', {'surveys': surveys})