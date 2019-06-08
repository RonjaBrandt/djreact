from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Survey app homepage</h1>")

def detail(request, survey_id):
    return HttpResponse("<h2>This is the DETAILVIEW for survey with id: " 
    + str(survey_id + "</h2>"))