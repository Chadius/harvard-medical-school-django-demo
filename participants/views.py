from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("participants index.")
    
# TODO: Add a view to add a new participant. Make sure it looks at post requests.
# TODO: Views! https://docs.djangoproject.com/en/1.9/intro/tutorial03/