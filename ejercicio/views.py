from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'ejercicio/home.html',{'nombre':'Carlos Ruiz'})

def otra_pagina(request):
    return HttpResponse('<h1>Other page</h1>')