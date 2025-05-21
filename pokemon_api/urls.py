from django.urls import path

from pokemon_api.views import PokemonApiView, PokemonManagementView, PokemonScoreView

urlpatterns = [
    path('api/pokemon/', PokemonApiView.as_view(), name='pokemon-detail'),
    path('pokemon/', PokemonManagementView.as_view(), name='pokemon-management'),
    path('pokemon/<uuid:id>/', PokemonManagementView.as_view(), name='pokemon-management-detail'),
    path('pokemon/<uuid:id>/score/', PokemonScoreView.as_view(), name='pokemon-score'),
]
