from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello from view.py')

def bye(request):
    return HttpResponse('bye from view.py')
