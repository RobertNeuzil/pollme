from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = f"It is now {now}"
	return HttpResponse(html)

def hello(request):
	return HttpResponse ("<h1> Hello WOoooooRld </h1>")

def bye(request):
	return HttpResponse("<h1> Goodbye </h1>")

def news(request):
	return HttpResponse("<h1> Fake News </h1>")