from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is the Home Page of the Applciation</h1>')

# Create your views here.
