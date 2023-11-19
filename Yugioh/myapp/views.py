from django.shortcuts import render, HttpResponse
from .models import Cards
import requests

# Create your views here.
def home(request):
    cards = Cards.objects.all()
    yugioh = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").json()
    #print(yugioh)
    return render(request, "home.html", {"cards": cards, "yugioh": yugioh})