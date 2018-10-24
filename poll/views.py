from django.http import HttpResponse
from django.shortcuts import render
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = f"It is now {now}"
	return HttpResponse(html)

def home(request):
	now = datetime.datetime.now()
	context = {'datetimenow': now}

	return render(request, 'home.html', context)