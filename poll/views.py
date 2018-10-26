
from django.shortcuts import render
import datetime

def home(request):
	now = datetime.datetime.now()
	context = {'datetimenow': now}

	return render(request, 'home.html', context)


def pollhome(request):
	context = {}
	return render(request, 'pollhome.html', context)