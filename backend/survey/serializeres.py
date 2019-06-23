from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        #field = ('titlel', 'items')
        fields = '__all__'