from rest_framework import serializers
from .models import Survey, Category, Question

class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'category_Name', 'current_Points')

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'