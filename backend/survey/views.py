from django.views import generic
from .models import Surveys

class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'all_surveys'

    def get_queryset(self):
        return Surveys.objects.all()


class DetailView(generic.DetailView):
    model = Surveys
    template_name='survey/detail.html'