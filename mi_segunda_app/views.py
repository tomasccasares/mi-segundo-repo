from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}!')




