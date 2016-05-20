from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')

def cadastro(request):
	return render(request, 'cadastro.html')

def sobre(request):
	return render(request, 'sobre.html')

def detalhes(request):
	return render(request, 'detalhes.html')
