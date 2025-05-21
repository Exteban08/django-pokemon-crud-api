import logging

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon_api.serializers import PokemonSerializer
from pokemon_api.services.pokemon_api_service import PokemonApiService
from .models import Pokemon
from .services.score_service import ScoreService

logger = logging.getLogger(__name__)


class PokemonApiView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        pokemon_name = request.query_params.get('name')
        service = PokemonApiService()

        try:
            pokemon_details = service.get_pokemon_details(pokemon_name=pokemon_name)

            if not pokemon_details:
                return Response({"error": "Pokemon not found"}, status=status.HTTP_404_NOT_FOUND)

            formatted_data = service.format_pokemon_data(pokemon_details)
            return Response(formatted_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error fetching Pokemon data: {e}")
            return Response({"error": "An error occurred while fetching Pokemon data"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PokemonManagementView(GenericAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        name = request.query_params.get('name')

        if id:
            pokemon = get_object_or_404(self.get_queryset(), id=id)
            serializer = self.get_serializer(pokemon)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif name:
            pokemon = get_object_or_404(self.get_queryset(), name=name)
            serializer = self.get_serializer(pokemon)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            pokemons = self.get_queryset()
            serializer = self.get_serializer(pokemons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        pokemon = get_object_or_404(self.get_queryset(), id=id)
        serializer = self.get_serializer(pokemon, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        pokemon = get_object_or_404(self.get_queryset(), id=id)
        pokemon.delete()
        return Response({"message": f"Pokemon with id '{id}' deleted successfully."}, status=status.HTTP_200_OK)


class PokemonScoreView(APIView):
    score_service = ScoreService()

    def get(self, request, id=None):
        try:
            pokemon = get_object_or_404(Pokemon, id=id)

            base_stats_list = list(pokemon.base_stats.values())
            pokemon_data = {
                'types': pokemon.types,
                'base_stats': base_stats_list,
                'abilities': pokemon.abilities,
                'height': pokemon.height,
                'weight': pokemon.weight,
            }

            score = self.score_service.calculate_score(pokemon_data)

            return Response({
                'name': pokemon.name,
                'score': score
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error calculating score: {e}")
            return Response({"error": "An error occurred while calculating the score."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
