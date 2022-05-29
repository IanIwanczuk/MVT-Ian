from django.http import HttpResponse

from django.shortcuts import render

def prueba(request):
    return render(request, 'prueba.html', context = {})

def index(request):
    return render(request, 'index.html')
