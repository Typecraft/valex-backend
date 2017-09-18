from rest_framework import serializers

from lexicon.models import Lemma, Meaning, ValenceFrame, MeaningValence, Example
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('url', 'id', 'is_active', 'is_staff', 'is_superuser')


class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = ('url', 'id', 'lemma', 'meanings', 'citationForm', 'comment', 'language',)


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
