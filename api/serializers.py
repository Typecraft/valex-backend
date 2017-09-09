from django.contrib.auth.models import User
from rest_framework import serializers

from lexicon.models import Lemma, Meaning, ValenceFrame, MeaningValence, Example


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email')
        read_only_fields = ('url', 'id')


class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = ('url', 'id', 'lemma', 'meanings',)


class MeaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meaning
        fields = ('url', 'id', 'meaning', 'ontologyToken', 'lemma', 'valences',)


class ValenceFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValenceFrame
        fields = ('url', 'id', 'name', 'description',)


class MeaningValenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeaningValence
        fields = ('url', 'id', 'meaning', 'valenceFrame', 'examples')


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('url', 'id', 'meaningValence', 'text', 'link')
