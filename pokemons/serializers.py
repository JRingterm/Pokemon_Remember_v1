from rest_framework import serializers
from .models import Pokemon

class LookupSerializer(serializers.ModelSerializer): #전체조회 시리얼라이저
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'teratype', 'ability', 'stats', 'item', 'description')

class DetailCreateSerializer(serializers.ModelSerializer): #상세조회, 생성 시리얼라이저
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'nature', 'ability', 'teratype', 'stats', 'skills', 'item', 'description')
