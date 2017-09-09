import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

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


@csrf_exempt
def api_token_auth_session(request):
    if not request.user.is_authenticated:
        return HttpResponse(
            json.dumps({'detail': 'Not logged in'}),
            content_type='application/json',
            status=status.HTTP_403_FORBIDDEN
        )

    token = request.user.auth_token
    if token is None:
        token = Token(user=request.user)
        token.save()

    return HttpResponse(
        json.dumps({'token': token.key}),
        content_type='application/json',
        status=status.HTTP_200_OK
    )
