from django.db import models

# Create your models here.


class Lemma(models.Model):
    LANGUAGE_CHOICES = (
        ('nob', 'Norwegian'),
        ('deu', 'German')
    )
    lemma = models.CharField(max_length=255)
    language = models.CharField(max_length=4, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.lemma


class Meaning(models.Model):
    meaning = models.CharField(max_length=511, blank=True, default='')
    lemma = models.ForeignKey(Lemma, on_delete=models.CASCADE, related_name='meanings')
    ontologyToken = models.CharField(default='', blank=True, max_length=4)

    def __str__(self):
        return self.meaning


class ValenceFrame(models.Model):

    name = models.CharField(blank=True, default='', max_length=128)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class MeaningValence(models.Model):
    meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE, related_name='valences')
    valenceFrame = models.ForeignKey(ValenceFrame, null=True, on_delete=models.SET_NULL, related_name='examples')

    def __str__(self):
        return "Valence %s of meaning %s" % (str(self.valenceFrame), str(self.meaning))


class Example(models.Model):
    meaningValence = models.ForeignKey(MeaningValence, on_delete=models.CASCADE, related_name='examples')
    text = models.TextField(blank=True, default='')
    link = models.TextField(blank=True, default='')

    def __str__(self):
        return "Example %d for meaningValence %d" % (self.id, self.id)
