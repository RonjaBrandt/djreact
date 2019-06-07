from django.http import HttpResponse
from django.conf import settings

import requests

def save_survey(request):

   url="https://api.typeform.com/forms/nv4fXG/responses"
   headers = {'Authorization': 'Bearer 94HyzhMYCbSZyAczo6xXi7GZuFLRuvUA9krjC9FFahUf'}
   r = requests.get(url, headers=headers)¨
   data = json.load(request.body)
   
   

   return HttpResponse("se if get respons in consol" + str(r.json()))