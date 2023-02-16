import requests
from .models import Pokemon, Type
from concurrent.futures import ThreadPoolExecutor
from typing import Any
from django.db import transaction


class DataRetriever:
    def get_list(self, url_end: str) -> list[dict[str, Any]]:
        data = requests.get(f"https://pokeapi.co/api/v2/{url_end}?limit=1000").json()
        my_list = data["results"]
        while True:
            if data["next"] is None:
                break
            data = requests.get(data["next"]).json()
            my_list.extend(data["results"])
        return my_list

    def get_poke_types(self):
        identifiers = [poke.identifier for poke in Pokemon.objects.all()]
        with ThreadPoolExecutor() as ex:
            datas = ex.map(
                lambda identifier: requests.get(
                    f"https://pokeapi.co/api/v2/pokemon/{identifier}/"
                ).json(),
                identifiers,
            )
        dico_types = {
            data["id"]: [poke_type["type"]["name"] for poke_type in data["types"]]
            for data in datas
        }
        return dico_types


class DataSaver:
    def save_list(self, table, url_end):
        data_retriever = DataRetriever()
        infos = data_retriever.get_list(url_end)
        table_objects = []
        for info in infos:
            identifier = info["url"].split("/")[-2]
            table_objects.append(table(name=info["name"], identifier=identifier))
        table.objects.bulk_create(table_objects)

    def save_poke_types(self):
        data_retriever = DataRetriever()
        dico_types = data_retriever.get_poke_types()
        dico_type = {poke_type.name: poke_type.pk for poke_type in Type.objects.all()}
        dico_poke = {pokemon.identifier: pokemon for pokemon in Pokemon.objects.all()}
        with transaction.atomic():
            for identifier, poke_types in dico_types.items():
                poke = dico_poke[identifier]
                ids = [dico_type[poke_type] for poke_type in poke_types]
                poke.type.add(*ids)
