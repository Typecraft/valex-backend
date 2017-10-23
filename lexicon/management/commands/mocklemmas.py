import json
import os
from django.core.management import BaseCommand

from lexicon.models import Lemma


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(os.path.dirname(__file__), 'lemmas.json'), encoding="utf-8") as f:
            lemmas = json.load(f)
            Lemma.objects.bulk_create([
                Lemma(
                    lemma=lemma,
                    language='deu'
                ) for lemma in lemmas
            ])


