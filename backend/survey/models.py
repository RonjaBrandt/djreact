from django.db import models
from django.urls import reverse

class Surveys(models.Model):
   # Takes in all the data
   titlel = models.CharField(max_length=500, default="Something defult titel")
   items = models.CharField(max_length=500, default="Something defult item")

   def get_absolute_url(self):
      return reverse('survey:detail', kwargs={'pk':self.pk})

   def __str__(self):
      return '//Titlel: ' + self.titlel + ' //Item: ' + self.items



class Questions(models.Model):
    surveys = models.ForeignKey(Surveys, on_delete=models.CASCADE, default=2)
    answers = models.TextField(max_length=500, default="Something defult ansewr")
    is_results = models.BooleanField(default=False)
    def __str__(self):
      return self.answers