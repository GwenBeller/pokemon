from pokedex.models import Pokemon, Type
from rest_framework import generics
from .serializer import PokemonSerializer, TypeSerializer



class PokemonList(generics.ListAPIView):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializer
    
class PokemonDetail(generics.RetrieveAPIView):
    queryset=Pokemon.objects.all()
    serializer_class=PokemonSerializer
    
class TypeList(generics.ListAPIView):
    queryset=Type.objects.all
    serializer_class=TypeSerializer
    
class TypeDetail(generics.RetrieveAPIView):
    queryset=Type.objects.all()
    serializer_class=TypeSerializer