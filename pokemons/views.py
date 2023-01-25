from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Pokemon
from .serializers import LookupSerializer, DetailCreateSerializer

# Create your views here.
class PokemonsAPIView(APIView): #전체조회 뷰
    def get(self, request): #조회
        pokemons = Pokemon.objects.all()
        serializer = LookupSerializer(pokemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request): #생성
        serializer = DetailCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonAPIView(APIView): #상세조회 뷰 (1개 가져오기)
    def get(self, request, pk): #데이터 가져오기
        pokemon = get_object_or_404(Pokemon, id=pk)
        serializer = DetailCreateSerializer(pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk): #데이터 수정하기
        pokemon = Pokemon.objects.get(id=pk)
        serializer = DetailCreateSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): #데이터 삭제
        pokemon = Pokemon.objects.get(id=pk)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

