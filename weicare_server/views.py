from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def index(request):
    return JsonResponse( {"message": "Hello, world. You're at the weicare server index." }, safe = False)







