from django.db import models

# Create your models here.


class Lemma(models.Model):
    LANGUAGE_CHOICES = (
        ('nob', 'Norwegian'),
        ('deu', 'German')
    )
    lemma = models.CharField(max_length=255)
    language = models.CharField(max_length=4, choices=LANGUAGE_CHOICES)


class Meaning(models.Model):
    meaning = models.TextField()
    lemma = models.ForeignKey(Lemma, on_delete=models.CASCADE)
    ontologyToken = models.CharField(max_length=4)


class ValenceFrame(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()


class MeaningValence(models.Model):
    meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE, related_name='valences')
    valenceFrame = models.ForeignKey(ValenceFrame, on_delete=models.CASCADE, related_name='examples')


class Example(models.Model):
    meaningValence = models.ForeignKey(MeaningValence, on_delete=models.CASCADE, related_name='examples')
    text = models.TextField()
    link = models.TextField()