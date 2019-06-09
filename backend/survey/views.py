from django.shortcuts import render, get_object_or_404
from .models import Surveys

def index(request):
    all_surveys = Surveys.objects.all()
    context = {'all_surveys': all_surveys} 
    return render(request, 'survey/index.html', context)

def detail(request, surveys_id):
    surveys = get_object_or_404(Surveys, pk=surveys_id)
    return render(request, 'survey/detail.html', {'surveys': surveys})