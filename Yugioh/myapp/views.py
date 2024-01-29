from django.shortcuts import render, HttpResponse
from .models import Cards
import requests

# Create your views here.
def home(request):
    cards = Cards.objects.all()
    yugioh = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").json()
    #print(yugioh)
    return render(request, "home.html", {"cards": cards, "yugioh": yugioh})

def search(request):
    #cards = Cards.objects.all()
    query = request.GET.get("fname")
    yugioh = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?fname=" + query).json()
    return render(request, "search.html", {"yugioh": yugioh, "query": query})

def watchlist(request):
    return render(request, "watchlist.html")
