import json
import random

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from api.serializers import UserSerializer, LemmaSerializer, MeaningSerializer, ValenceFrameSerializer, \
    MeaningValenceSerializer, ExampleSerializer
from lexicon.models import ValenceFrame, Meaning, Lemma, Example, MeaningValence
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'current':
            return self.request.user

        return super(UserViewSet, self).get_object()


class LemmaViewSet(viewsets.ModelViewSet):
    queryset = Lemma.objects.all().order_by('lemma')
    serializer_class = LemmaSerializer
    filter_fields = {
        'lemma': ['exact', 'contains', 'icontains', 'startswith'],
        'comment': ['exact', 'contains', 'icontains', 'startswith'],
    }


class MeaningViewSet(viewsets.ModelViewSet):
    queryset = Meaning.objects.all().order_by('meaning')
    serializer_class = MeaningSerializer
    filter_fields = {
        'meaning': ['exact', 'contains', 'icontains', 'startswith'],
        'lemma': ['exact']
    }


class ValenceFrameViewSet(viewsets.ModelViewSet):
    queryset = ValenceFrame.objects.all().order_by('name')
    serializer_class = ValenceFrameSerializer
    filter_fields = {
        'name': ['exact', 'contains', 'icontains', 'startswith'],
        'description': ['exact', 'contains', 'icontains', 'startswith'],
    }


class MeaningValenceViewSet(viewsets.ModelViewSet):
    queryset = MeaningValence.objects.all().order_by('meaning', 'valenceFrame__name')
    serializer_class = MeaningValenceSerializer
    filter_fields = ('meaning', 'valenceFrame',)


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all().order_by('text')
    serializer_class = ExampleSerializer
    filter_fields = {
        'text': ['exact', 'contains', 'icontains', 'startswith'],
    }


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


@api_view(['GET'])
def lemma_of_the_day(request):
    count = Lemma.objects.aggregate(count=Count('id'))['count']
    today = timezone.now().date()
    random.seed(today.year + today.month + today.day)
    lemma = Lemma.objects.all()[random.randint(0, count-1)]
    serializer = LemmaSerializer(lemma, context={'request': request})
    return Response(
        serializer.data
    )

