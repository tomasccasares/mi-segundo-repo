from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.

def mensaje(request, mensaje):
    return HttpResponse(f'Hola! este es tu mensaje: {mensaje}')

def edad(request, edad):
    pass
    


    
        
            


    


