from django.views import generic
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Surveys
from .forms import JoinForm
from .mixins import AjaxFormMixin


#En model.Model är ditt interface mot databasen. En View är ett sätt att visa data, eller ta emot.##

class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name  = 'forms/ajax.html'
    success_url = '/form-success/'


class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'all_surveys'        

    def get_queryset(self):
        return Surveys.objects.all()


class DetailView(generic.DetailView):
    model = Surveys
    template_name='survey/detail.html'

# TROLIGEN ÄR DET HÄR SOM JSON DATA SKA IN PÅ NÅGOT SÄTT
class SurveyCreate(CreateView):
    model = Surveys
    fields = ['titlel', 'items']


''' Get JSON working but dont know where to put it
 def save_survey(request):
        url="https://api.typeform.com/forms/nv4fXG/responses"
        headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf'}
        response = requests.get(url, headers=headers)
        '''
#Lista all survey api not working
''' REST API -NOT WORKING-
class SurveysList(APIView):

    def get(self, request):
        surveys = Surveys.objects.all()
        serializer = SurveysSerializer(surveys, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
'''