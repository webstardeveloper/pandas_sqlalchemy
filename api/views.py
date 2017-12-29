from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    template_name = "demo.html"
    return render(request, template_name, {})

def filter_by_country(request):
    
    return JsonResponse({'result': target_score})

def filter_by_artist(request):
    
    return JsonResponse({'result': target_score})
