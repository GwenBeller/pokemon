from typing import Any

from django.core.management.base import BaseCommand

from pokedex.utils import DataSaver


class Command(BaseCommand):
    help = "Populate types for each pokemon"

    def handle(self, *args: Any, **options: Any) -> None:
        DataSaver().save_poke_types()
