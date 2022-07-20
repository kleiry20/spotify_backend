from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request, *args, **kwargs): 
    return JsonResponse({"name": "index"})
