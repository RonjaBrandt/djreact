from django.http import HttpResponse
from django.template import loader
from .models import Survey

def index(request):
    all_survey = Survey.objects.all()
    template = loader.get_template('survey/index.html')
    context = {
        'all_survey': all_survey,
    } 
    return HttpResponse(template.render(context, request))

def detail(request, survey_id):
    return HttpResponse("<h2>This is the DETAILVIEW for survey with id: " 
    + str(survey_id + "</h2>"))