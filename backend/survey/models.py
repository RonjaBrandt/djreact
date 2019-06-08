from django.db import models


class Survey(models.Model):
   # Takes in all the data
   items = models.CharField(max_length=500)

   def __str__(self):
       return '----BEGINING---- ' + self.items + ' ---- END-----'

class Questions(models.Model):
    items = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_answers = models.CharField(max_length=500)