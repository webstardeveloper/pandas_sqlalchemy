from django.shortcuts import render
from .models import Data
from AudioPlayer import settings

# Create your views here.

def index(request):
    template_name = "demo.html"
    '''countries = Data.objects.order_by('country').values('country').distinct()
    countries = [country['country'] for country in countries if country['country'] != None]'''

    countries = settings.COUNTRY

    '''artists = Data.objects.order_by('artist_gid').values('artist_gid').distinct()
    artists = [artist['artist_gid'] for artist in artists if artist['artist_gid'] != None]'''
    artists = ['31940d879ac54c7381a4fb4bff9a647d', 'd6122088de5a423ca001743f2c2d654a', 'ec5582c42eaa4bdabf4b8774457c023d']
    return render(request, template_name, {'countries': countries, 'artists': artists})

def filter_by_country(request):
    
    return JsonResponse({'result': target_score})

def filter_by_artist(request):
    
    return JsonResponse({'result': target_score})
