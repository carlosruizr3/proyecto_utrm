from django.http.response import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'ejercicio/home.html',{'nombre':'Carlos Ruiz'})

def nueva(request):
    return render(request,'ejercicio/nuevapaguina.html')
    
def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('!"#$%&/()='))
    length =  int(request.GET.get('length',8))
    pswd = ''
    for x in range(length):
        pswd +=  random.choice(caracteres)
    return render(request,'ejercicio/password.html',{'password':pswd})

