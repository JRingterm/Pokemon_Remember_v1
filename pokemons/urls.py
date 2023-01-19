from django.urls import path
from .views import PokemonsAPIView, PokemonAPIView

urlpatterns = [
    path('', PokemonsAPIView.as_view()),
    path('<int:pk>/', PokemonAPIView.as_view()),
]