from django.contrib import admin

# Register your models here.
from lexicon.models import Lemma, Meaning, MeaningValence, ValenceFrame, Example

admin.site.register(Lemma)
admin.site.register(Meaning)
admin.site.register(MeaningValence)
admin.site.register(Example)
