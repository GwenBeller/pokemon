from rest_framework import serializers
from pokedex.models import Pokemon, Type, Move


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
