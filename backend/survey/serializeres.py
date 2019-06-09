from rest_framework import serializers
from .models import Surveys

class SurveysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Surveys
        #field = ('titlel', 'items')
        fields = '__all__'