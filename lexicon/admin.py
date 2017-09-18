from django.contrib import admin

# Register your models here.
from lexicon.models import Lemma, Meaning, MeaningValence, ValenceFrame, Example


class MeaningInline(admin.TabularInline):
    model = Meaning


class MeaningValenceInline(admin.TabularInline):
    model = MeaningValence


class ExampleInline(admin.TabularInline):
    model = Example


class ValenceFrameInline(admin.TabularInline):
    model = ValenceFrame


class LemmaAdmin(admin.ModelAdmin):
    inlines = [
        MeaningInline
    ]


class MeaningAdmin(admin.ModelAdmin):
    inlines = [
        MeaningValenceInline
    ]


class MeaningValenceAdmin(admin.ModelAdmin):
    inlines = [
        ExampleInline
    ]


admin.site.register(Lemma, LemmaAdmin)
admin.site.register(Meaning, MeaningAdmin)
admin.site.register(MeaningValence, MeaningValenceAdmin)
admin.site.register(Example)
admin.site.register(ValenceFrame)
