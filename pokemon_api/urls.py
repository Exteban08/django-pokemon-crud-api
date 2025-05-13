from django.urls import path

from pokemon_api.views import PokemonViewSet, PokemonCreateView, PokemonUpdateView, PokemonDeleteView, \
    PokemonRetrieveView, PokemonListView, PokemonScoreView

urlpatterns = [
    path('api/pokemon/<str:name>', PokemonViewSet.as_view(), name='pokemon-detail'),
    path('pokemon/create/', PokemonCreateView.as_view(), name='pokemon-create'),
    path('pokemon/update/<str:name>', PokemonUpdateView.as_view(), name='pokemon-update'),
    path('pokemon/delete/<str:name>', PokemonDeleteView.as_view(), name='pokemon-delete'),
    path('pokemon/<str:name>', PokemonRetrieveView.as_view(), name='get-pokemon'),
    path('pokemon/list/', PokemonListView.as_view(), name='pokemon-list'),
    path('pokemon/scores/', PokemonScoreView.as_view(), name='pokemon-scores'),
]
