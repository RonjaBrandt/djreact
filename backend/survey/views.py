from django.http import HttpResponse
from .models import Survey

def index(request):
    all_survey = Survey.objects.all()
    html = ''
    for survey in all_survey:
        url ='/survey/' + str(survey.id) + '/'
        html += '<a href="' + url + '">' + survey.items + '</a><br>'
        pass
    return HttpResponse(html)

def detail(request, survey_id):
    return HttpResponse("<h2>This is the DETAILVIEW for survey with id: " 
    + str(survey_id + "</h2>"))