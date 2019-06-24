from django.db import models
from django.urls import reverse
from django.db.models import Max

class Survey(models.Model):
   survey_Id = models.CharField(max_length=20, help_text="Add the Survey ID from Typefrom here")
   
   def __str__(self):
      return 'SurveyID: '+self.survey_Id
   # TODO: Skapa Read-only fält för current points
class Category(models.Model):
    survey = models.ForeignKey(Survey, related_name='catagory', on_delete=models.CASCADE, help_text="Choose what Survey thos Category belogs to." , blank=True, null=True)
    category_Name = models.CharField(max_length=20, help_text="Name of the Catagory", blank=True, null=True)
    max_Points = models.DecimalField(max_digits=3, decimal_places=1, default=0, help_text="Maximum points for this catagory", blank=True, null=True)
    current_Points = models.DecimalField(max_digits=2, decimal_places=1, default=0, help_text="Displaying current points. DO NOT CHANGE THIS.", blank=True, null=True)
    

    def __str__(self):
       return 'Category: '+ self.category_Name + ' - ' + str(self.survey)


class Question(models.Model):
   # Menu for type of questions
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

   category = models.ForeignKey(Category, related_name='question', on_delete=models.CASCADE,help_text="Choose to what Category this question belongs to" ,blank=True, null=True)
   question_ID = models.CharField(max_length=500, help_text="Add the Question ID from Typefrom goes here", blank=True, null=True)
   question_Type = models.CharField(max_length=20, choices=typeChoices, help_text="Important that this is right")
   question_Answer = models.CharField(max_length=500, help_text="Important that this is exact", blank=True, null=True)
   question_Points = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0, help_text='Make sure that this is not higher then Max Points for the catagory. {Category.max_Points}' )
   
   def get_absolute_url(self):
      #send user to page that display the detiels of the input data
      return reverse('question:detail', kwargs={'pk':self.pk})
   
   def __str__(self):
      return 'QuestionID: ' + self.question_ID + ' - ' + str(self.category.survey)
