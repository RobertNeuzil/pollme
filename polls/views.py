from django.shortcuts import render
from django.http import HttpResponse

def polls_list(request):
	return render(request, 'polls/polls_list.html' )

# Create your views here.
