from django.db import models
from django.urls import reverse
from django.db.models import Max

class Survey(models.Model):
   survey_Id = models.CharField(max_length=20, default='The Survyes ID here plz')
   
   def __str__(self):
      return self.surveyid


class Question(models.Model):
   # Takes in all the data
   #Menu for type of questions
   shortText = 'text'
   longText = 'text'
   dropdown = 'text'
   multipleChoiceSingleOption = 'choice.label'
   multipleChoiceMultipleOptions = 'choice.labels'
   pictureChoiceSingleOption = 'choice.label'
   pictureChoiceMultipleOptions = 'choice.labels'
   email = 'email'
   website = 'url'
   fileUpload = 'file_url'
   legal = 'boolean'
   yesNo = 'boolan'
   rating = 'number'
   optionScale = 'number'
   number = 'number'
   date = 'date'
   typeChoices = (
      (shortText, 'short_text'),
      (longText, 'long_text'),
      (dropdown, 'dropdown'),
      (multipleChoiceSingleOption, 'multiple_choice (single option)'),
      (multipleChoiceMultipleOptions, 'multiple_choice (multiple options)'),
      (pictureChoiceSingleOption, 'picture_choice (single option)'),
      (pictureChoiceMultipleOptions, 'picture_choice (multiple options)'),
      (email, 'email'),
      (website, 'website'),
      (fileUpload, 'file_upload'),
      (legal, 'legal'),
      (yesNo, 'yes_no'),
      (rating, 'rating'),
      (optionScale, 'opinion_scale'),
      (number, 'number'),
      (date, 'date'),
   )

   survey = models.ForeignKey(Survey, on_delete=models.CASCADE,help_text="Choose to what Survey this question belongs to" ,blank=True, null=True)
   question_ID = models.CharField(max_length=500, help_text="Question ID from Typefrom goes here", blank=True, null=True)
   question_Type = models.CharField(max_length=20, choices=typeChoices, help_text="Important that this is right")
   question_Answer = models.CharField(max_length=500, help_text="Important that this is exact", blank=True, null=True)
   question_Points = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0)
   

   def get_absolute_url(self):
      #send user to page that display the detiels of the input data
      return reverse('question:detail', kwargs={'pk':self.pk})
   
   def __str__(self):
      return 'QuestionID: ' + self.questionID + ' -SurveyID: ' +self.survey



   #Better naming?
class Score(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=True, null=True)
    verksamhetsstyrning = models.IntegerField(blank=True, default=0, help_text="Don't change this value")
    engagemang =  models.IntegerField(blank=True, default=0, help_text="Don't change this value")
    resurser =  models.IntegerField(blank=True,  default=0, help_text="Don't change this value")
    kommunikation =  models.IntegerField(blank=True, default=0, help_text="Don't change this value")

    def __str__(self):
       return 'Score to SurveyID: ' + str(self.survey)
    

    