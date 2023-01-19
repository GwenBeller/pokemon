import requests
from .models import Pokemon, Type
from django.db import IntegrityError


class DataRetriever:
    def get_list(self, url_end):
        data=requests.get(f"https://pokeapi.co/api/v2/{url_end}/").json()
        my_list=data["results"]
        while True:
            if data["next"] is None:
                break
            data=requests.get(data["next"]).json()
            my_list.extend(data["results"])
        return my_list
    
    # def get_poke_attributes(self, attribute):
    #     nb=Pokemon.objects.count()
    #     my_list=[]
    #     for i in range(1,nb+1):
    #         data=requests.get(f"https://pokeapi.co/api/v2/{i}/").json()
    #         for j in range(1,len(data[attribute])+1):
    #             my_list.extend(data[attribute][j])
    def get_poke_types(self):
        list_poke=Pokemon.objects.all()
        dico_types={}
        for poke in list_poke:
            identifier=poke.identifier
            print(identifier)
            data=requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifier}/").json()
            my_list_poke=[]
            for poke_type in data["types"]:
                my_list_poke.append(poke_type["type"]["name"])
            dico_types[identifier]=my_list_poke
        return dico_types
        
class DataSaver:
    def save_list(self, table, url_end):
        data_retriever=DataRetriever()
        infos=data_retriever.get_list(url_end)
        for info in infos:
            identifier=info["url"].split("/")[-2]
            try:
                table.objects.create(name=info["name"], identifier=identifier)
            except IntegrityError:
                pass
            
    def save_poke_types(self):
        data_retriever=DataRetriever()
        dico_types=data_retriever.get_poke_types()
        list_poke=Pokemon.objects.all()
        for poke in list_poke:
            for poke_types in dico_types:
                for poke_type in poke_types:
                    poke.types.add(poke_type)