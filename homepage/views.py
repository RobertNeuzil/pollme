from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = f"It is now {now}"
	return HttpResponse(html)
# Create your views here.
