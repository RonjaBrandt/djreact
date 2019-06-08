from django.http import HttpResponse
from django.template import loader
from .models import Survey

def index(request):
    all_survey = Survey.objects.all()
    template = loader.get_template('')
    return HttpResponse()

def detail(request, survey_id):
    return HttpResponse("<h2>This is the DETAILVIEW for survey with id: " 
    + str(survey_id + "</h2>"))