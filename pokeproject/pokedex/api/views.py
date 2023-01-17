from pokedex.models import Pokemon
from rest_framework import generics
from .serializer import PokemonSerializer



class PokemonList(generics.ListAPIView):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializer
    
class PokemonDetail(generics.RetrieveAPIView):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializer