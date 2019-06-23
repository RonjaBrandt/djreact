from rest_framework import serializers
from .models import Survey, Category, Question

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        #field = ('titlel', 'items')
        fields = '__all__'