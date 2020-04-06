from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is the Home Page of the Applciation and the Build is 1.0.46 and Build number 46 and welcome</h1>')

# Create your views here.
