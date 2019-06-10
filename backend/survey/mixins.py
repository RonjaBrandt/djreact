from django.http import JsonResponse
import json
import requests
'''
class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
'''
class JsonFormMixin(object):
    #def form_invalid(self, form):
        #response = super(JsonFormMixin, self).form_invalid(form)
        #Valdition för Json

	def get_form_kwargs(self):
		return json.loads(self.request.body)

