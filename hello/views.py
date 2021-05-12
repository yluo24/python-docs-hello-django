from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello from Sara! This is a Web App on Azure")
