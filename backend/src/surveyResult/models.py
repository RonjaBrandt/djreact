from django.db import models

#Survey
class Survey(models.Model):
    # The model Survey takes out the information from Typefrom in JSON
    # from the array called "item[{}]"
    #
    # Takes out the respons id from the questioner.
    # ex: "cef954291edb8514c16e0e20bec03def"
    item_response_id = models.CharField(max_length=250),
    # Takes out the time that the survey was started
    # ex: 2019-05-10T00:06:28Z"
    item_landed_at = models.CharField(max_length=250),
    # Takes out the time the survey was submitted at
    # ex: "2019-05-10T00:07:09Z"
    item_submitted_at = models.CharField(max_length=250),
    # Takes out id/referens for the questioner from metadata
    # ex: "https://ronjabrandt.typeform.com/to/nv4fXG"
    # after last / is the id/referens but need the hole https
    item_metadata_referer = models.CharField(max_length=250),
    #Takes out id for network to help with get right survey
    # ex: "0cf28107c5"
    item_metadata_network_id = models.CharField(max_length=250),
##########################################################################
# 1 Survey to many Questions
##########################################################################
#Question
class Question(models.Model):

##########################################################################
# 1 Question to many Answers
##########################################################################
#Answer
##########################################################################
# 1 Answer to many Points
##########################################################################
#Points