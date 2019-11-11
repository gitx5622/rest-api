from rest_framework import serializers
from .models import Language,Paradigm,Programmer


class ParadigmSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id','url','name')

class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','url','name','paradigm')


class ProgrammerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','url','name','languages')

