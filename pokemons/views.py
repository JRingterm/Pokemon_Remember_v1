from rest_framework import viewsets #filter가 viewset에서만 먹히는거 같음..
from rest_framework.generics import get_object_or_404
from .models import Pokemon
from .serializers import LookupSerializer, DetailCreateSerializer

# Create your views here.
class PokemonsAPIView(viewsets.ModelViewSet): #전체조회 뷰 APIView는 filter가 안먹혀서 viewsets으로 변경.
    queryset = Pokemon.objects.all()
    serializer_class = LookupSerializer
    filterset_fields = ['name']

    def get_serializer_class(self): #오버라이드. 메소드에 따라 시리얼라이저 변경함.
        if self.action in ("list"):
            return LookupSerializer
        if self.action in ("create", "retrieve", "update"):
            return DetailCreateSerializer
            
        return LookupSerializer


