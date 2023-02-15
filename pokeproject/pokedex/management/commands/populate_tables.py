from django.core.management.base import BaseCommand
from pokedex.utils import DataSaver
from pokedex.models import Pokemon
from pokedex.models import Type
from typing import Any


class Command(BaseCommand):
    help = "Delete and populate tables"

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Delete pokemons")
        Pokemon.objects.all().delete()
        self.stdout.write("Populate pokemons")
        DataSaver().save_list(Pokemon, "pokemon")
        self.stdout.write("Delete types")
        Type.objects.all().delete()
        self.stdout.write("Populate types")
        DataSaver().save_list(Type, "type")
