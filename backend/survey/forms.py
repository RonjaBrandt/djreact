from django import forms

class JoinForm(forms.Form):

    #Takes in all the data   
    item = forms.CharField(max_length=600)

    def __str__(self):
        return 'Respons ID: ' + self.item
   
    # The model Survey takes out the information from Typefrom in JSON
    # from the array called "item"
    #
    # Takes out the respons id from the questioner.
    # ex: "response_id": "cef954291edb8514c16e0e20bec03def"
    #response_id = models.CharField(max_length=250),
     #
    # Takes out the time that the survey was started
    # ex: "landed_at": "2019-05-10T00:06:28Z",
    #landed_at = models.CharField(max_length=250),
    #
    # Takes out the time the survey was submitted at
    # ex: "submitted_at": "2019-05-10T00:07:09Z",
    #submitted_at = models.CharField(max_length=250),
    #
    # Takes out id/referens for the questioner from metadata
    # After last / is the id/referens but need the survey
    # ex: "referer": "https://ronjabrandt.typeform.com/to/nv4fXG",
    #metadata_referer = models.CharField(max_length=250),
    #
    # Takes out id for network to help with get right survey
    # ex: "network_id": "0cf28107c5",
    #metadata_network_id = models.CharField(max_length=250)
    #
    # #Print out info:
   # def __str__(self):
    #    return 'Respons ID: ' + self.item_response_id + ' -Start Time: ' + self.item_landed_at + ' -End Time: ' + #self.item_submitted_at + ' -HTTPadress/survey ID;: ' + self.item_metadata_referer + ' -NetworkID: ' + #self.item_metadata_referer + ' -end- '

 ##########################################################################
 # 1 Survey to many Answers
 ##########################################################################
 #Answers
 #class Answers(models.Model):
    # The model Answer takes out object from Typeform in JSON
    # from the array called "answers"
    #
    # If the survey is deleted then delete the answer to that survey
    ##survey = models.ForeignKey(Survey, on_delete=models.CASCADE),
    
    #
    # Takes out the id for question
    # ex: "id": "ovmiTI7jMvHR",
    #field_id = models.CharField(max_length=250),
    #
    # Takes out the type of question
    # ex: "type": "multiple_choice", 
    # or
    # ex: "type": "rating",
    #field_type = models.CharField(max_length=250),
    #
    # Takes out the referens for question
    # ex: "ref": "79bbd17cee403288"
    #field_ref = models.CharField(max_length=250),
    #
    # Takes out the type for Answers
    # ex: 'type': 'choice',
   # answers_type = models.CharField(max_length=250),
    #
    # Takes out the respons for Answers
    # ex:"choices": {
    #            "labels": ["Walking"]
    #       }
    # or
    # ex: "text": "Sweden"
    #answers_type_choice = models.CharField(max_length=250),
    #answers_type_text = models.CharField(max_length=250),
    #answers_type_number = models.CharField(max_length=250),
    #answers_type_label = models.CharField(max_length=250),
    #TODO: Gör så att programmet känner av olika fällt, alt en kategori för varje typ av svar
    #
    #Print out:

   #def __str__(self):
      # return
       
       
       #return 'Respons ID: ' + self.item_response_id + ' -Start Time: ' + self.item_landed_at + ' -End Time: ' + self.item_submitted_at + ' -HTTPadress/survey ID;: ' + self.item_metadata_referer + ' -NetworkID: ' + self.item_metadata_network_id + 'Question ID: ' + self.answers_field_id + ' -Question Type: ' + self.answers_field_type + ' -Question Referens: ' + self.answers_field_ref + ' -Answer Type: ' + self.answers_type + ' -Choice: ' + self.answers + ' -end- '

##########################################################################
# 1 Answer to many Points
##########################################################################
#Points
