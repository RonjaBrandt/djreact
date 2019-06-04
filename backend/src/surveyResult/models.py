from django.db import models

#Survey
class Survey(models.Model):
    # The model Survey takes out the information from Typefrom in JSON
    # from the array called "item"
    #
    # Takes out the respons id from the questioner.
    # ex: "response_id": "cef954291edb8514c16e0e20bec03def"
    item_response_id = models.CharField(max_length=250),
    #
    # Takes out the time that the survey was started
    # ex: "landed_at": "2019-05-10T00:06:28Z",
    item_landed_at = models.CharField(max_length=250),
    #
    # Takes out the time the survey was submitted at
    # ex: "submitted_at": "2019-05-10T00:07:09Z",
    item_submitted_at = models.CharField(max_length=250),
    #
    # Takes out id/referens for the questioner from metadata
    # After last / is the id/referens but need the survey
    # ex: "referer": "https://ronjabrandt.typeform.com/to/nv4fXG",
    item_metadata_referer = models.CharField(max_length=250),
    #
    #Takes out id for network to help with get right survey
    # ex: "network_id": "0cf28107c5",
    item_metadata_network_id = models.CharField(max_length=250)
    #
##########################################################################
# 1 Survey to many Answers
##########################################################################
#Answers
class Answers(models.Model):
    # The model Answer takes out object from Typeform in JSON
    # from the array called "answers"
    #
    #If the survey is deleted then delete the answer to that survey
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE),
    #
    # Takes out the id for question
    # ex: "id": "ovmiTI7jMvHR",
    answers_field_id = models.CharField(max_length=250),
    #
    # Takes out the type of question
    # ex: "type": "multiple_choice", 
    # or
    # ex: "type": "rating",
    answers_field_type = models.CharField(max_length=250),
    #
    # Takes out the referens for question
    # ex: "ref": "79bbd17cee403288"
    answers_field_ref = models.CharField(max_length=250),
    #
    # Takes out the type for Answers
    # ex: 'type': 'choice',
    answers_type = models.CharField(max_length=250),
    #
    # Takes out the respons for Answers
    # ex:"choices": {
    #            "labels": ["Walking"]
    #       }
    # or
    # ex: "text": "Sweden"
    #TODO: Gör så att programmet känner av olika fällt, alt en kategori för varje typ av svar
    answers_type = models.CharField(max_length=250),
    #
    
##########################################################################
# 1 Answer to many Points
##########################################################################
#Points