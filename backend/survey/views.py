from django.shortcuts import render, get_object_or_404
from .models import Surveys, Questions

def index(request):
    all_surveys = Surveys.objects.all()
    context = {'all_surveys': all_surveys} 
    return render(request, 'survey/index.html', context)

def detail(request, surveys_id):
    surveys = get_object_or_404(Surveys, pk=surveys_id)
    return render(request, 'survey/detail.html', {'surveys': surveys})

def results(request, surveys_id):
    surveys = get_object_or_404(Surveys, pk=surveys_id)
    try:
        selected_question = surveys.questions_set.get(pk=request.POST['questions'])
    except (KeyError, Questions.DoesNotExist):
        return render(request, 'survey/index.html', {
            'surveys': surveys,
            'error_message': "You did not select any question",
        })
    else:
        selected_question.is_results = True
        selected_question.save()
        return render(request, 'survey/detail.html', {'surveys': surveys})