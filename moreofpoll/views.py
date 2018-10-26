from django.shortcuts import render


def pollhome(request):
	return render(request, 'pollhome.html', context)

# Create your views here.
