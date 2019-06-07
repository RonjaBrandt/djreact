from django.forms import ModelForm
from .models import Survey

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fieds = ['item_response_id', 'item_landed_at', 'item_submitted_at', 'item_metadata_referer', 'item_metadata_network_id', 'answers_field_id', 'answers_field_type', 'answers_field_ref', 'answers_type','answers']