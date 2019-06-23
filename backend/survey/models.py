from django.db import models
from django.urls import reverse

class Survey(models.Model):
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

 
   questionID = models.CharField(max_length=500, default="Question ID from Typefrom goes here")
   questionType = models.CharField(max_length=20, choices=typeChoices)
   questionAnswer = models.CharField(max_length=500, default="Exact answer goes here")
   questionMaxPoints = models.IntegerField(default=0)
   questionPoints = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0)
   

   def get_absolute_url(self):
      #send user to page that display the detiels of the input data
      return reverse('survey:detail', kwargs={'pk':self.pk})




   #Better naming?
class Score(models.Model):
    verksamhetsstyrning = models.IntegerField(blank=True, default=0)
    engagemang =  models.IntegerField(blank=True, default=0)
    resurser =  models.IntegerField(blank=True,  default=0)
    kommunikation =  models.IntegerField(blank=True, default=0)

    def __str__(self):
      return self.answers