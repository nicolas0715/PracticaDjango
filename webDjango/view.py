from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"Hola")

def segunda_vista(request):
    return render(request, "segunda_vista.html")

def tercera_vista(request):
    return render("tercera_vista.html")

def cuarta_vista(request):
    return render("cuarta_vista.html")