from django.shortcuts import render
import requests
import json
from django.http import HttpResponse


# Create your views here.
TMBD_API_KEY="d903bcdae97d41411a8e54f49fb3b5d0"
def movise(request):
    
 
       
    data= requests.get(f'https://api.themoviedb.org/3/trending/all/day?api_key=d903bcdae97d41411a8e54f49fb3b5d0').json()
    #    temp=[]
    #    for m in data.json()['results']:
    #        if len(temp)<3:
    #            temp.append({'poster_path': m["poster_path"], 'rate:': m['rate']})
    #        else:
    #            results.append(temp)
    #    results.append(temp) if len(temp) >0 else None
    return render(request,'Movies.html',{"data":data}
       
    )