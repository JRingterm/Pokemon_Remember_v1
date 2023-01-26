from django.urls import path
from .views import PokemonsAPIView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('pokemons', PokemonsAPIView)
urlpatterns = router.urls