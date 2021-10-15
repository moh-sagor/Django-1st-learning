from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Index</h1> <a href = '/contact/'>Contact</a> ")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <a href = '/index/'>Index</a>")
