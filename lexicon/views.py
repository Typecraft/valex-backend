from django.shortcuts import render
from rest_framework import viewsets
from lexicon.models import Lemma, Meaning, ValenceFrame, MeaningValence, Example
from .serializers import LemmaSerializer, MeaningSerializer, \
    ValenceFrameSerializer, MeaningValenceSerializer, ExampleSerializer


class LemmaViewSet(viewsets.ModelViewSet):
    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer


class MeaningViewSet(viewsets.ModelViewSet):
    queryset = Meaning.objects.all()
    serializer_class = MeaningSerializer


class ValenceFrameViewSet(viewsets.ModelViewSet):
    queryset = ValenceFrame.objects.all()
    serializer_class = ValenceFrameSerializer


class MeaningValenceViewSet(viewsets.ModelViewSet):
    queryset = MeaningValence.objects.all()
    serializer_class = MeaningValenceSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
