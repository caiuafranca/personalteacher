from django.shortcuts import render
from django.http import HttpResponse
from .models import Plano

# Create your views here.
def index(request):
	planos = Plano.objects.all()
	context = {
		'planos': planos
	}
	return render(request, 'index.html', context)
