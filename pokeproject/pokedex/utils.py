import requests
from .models import Pokemon
from django.db import IntegrityError

class DataRetriever:
    def get_pokemons(self):
        url="https://pokeapi.co/api/v2/pokemon"
        data=requests.get(url).json()
        pokemons=data["results"]
        while True:
            data=requests.get(data["next"]).json()
            pokemons.extend(data["results"])
            if data["next"] is None:
                break
        return pokemons
            
class DataSaver:
    def save_pokemons(self):
        data_retriever=DataRetriever()
        pokemons=data_retriever.get_pokemons()
        for pokemon in pokemons:
            num=pokemon["url"].split("/")[-2]
            try:
                new_pokemon=Pokemon.objects.create(name=pokemon["name"], dex=num)
            except IntegrityError:
                pass