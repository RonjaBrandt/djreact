from django.db import models
import json

def get_data(request):
       if request.method == 'post':
          url="https://api.typeform.com/forms/nv4fXG/responses"
          headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf'}
          r = requests.get(url, headers=headers)
          items = r.json()
          items = JSODNField()
         #for landing_id in items['items']:

#Survey
class Survey(models.Model):
    # The model Survey takes out the information from Typefrom in JSON
    # from the array called "item"
    #
    # Takes out the respons id from the questioner.
    # ex: "response_id": "cef954291edb8514c16e0e20bec03def"
    item_response_id = models.CharField(max_length=250),

    
          
      