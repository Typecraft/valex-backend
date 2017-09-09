from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from api.serializers import UserSerializer, LemmaSerializer, MeaningSerializer, ValenceFrameSerializer, \
    MeaningValenceSerializer, ExampleSerializer
from lexicon.models import ValenceFrame, Meaning, Lemma, Example, MeaningValence


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'current':
            return self.request.user

        return super(UserViewSet, self).get_object()


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
