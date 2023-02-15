import requests

data_poke = requests.get("https://pokeapi.co/api/v2/pokemon/").json()
data_poke1 = requests.get("https://pokeapi.co/api/v2/pokemon/1/").json()

poke_key = data_poke.keys()
poke1_key = data_poke1.keys()
