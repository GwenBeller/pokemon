from typing import Any

from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, Type
from pokedex.utils import DataSaver


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
