from django.template import RequestContext
from django.shortcuts import render_to_response
import time

def home(request, template_name="home.html"):
	context = RequestContext(request)

	#process as is with json
	for num in range(0,100):
		print "{0}%".format(num)
		time.sleep(1)

	return render_to_response(template_name, context)