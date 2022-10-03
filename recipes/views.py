from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={'nome': 'João Dias'})


def sobre(request):
    return render(request, 'recipes/sobre.html', context={})


def contato(request):
    return HttpResponse('Contato 2')
