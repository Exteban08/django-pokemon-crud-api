import logging

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon_api.serializers import PokemonSerializer
from pokemon_api.services.pokemon_api_service import PokemonApiService
from .models import Pokemon
from .services.score_service import ScoreService

logger = logging.getLogger(__name__)


class PokemonViewSet(RetrieveAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = PokemonApiService()

    def get(self, request, name):
        try:
            logger.info(f"Fetching Pokemon details for: {name}")
            pokemon_details = self.service.get_pokemon_details(pokemon_name=name)

            if not pokemon_details:
                logger.warning(f"Pokemon not found: {name}")
                return Response({"error": "Pokemon not found"}, status=status.HTTP_404_NOT_FOUND)

            return JsonResponse(pokemon_details, safe=False)

        except Exception as e:
            logger.error(f"Error fetching Pokemon data: {e}", exc_info=True)
            return Response({"error": "An error occurred while fetching Pokemon data"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PokemonCreateView(CreateAPIView):
    serializer_class = PokemonSerializer

    def perform_create(self, serializer):
        name = self.request.data.get('name')

        if not name:
            raise ValidationError({"error": "The 'name' field is required."})

        if Pokemon.objects.filter(name=name).exists():
            raise ValidationError({"error": f"Pokemon with name '{name}' already exists."})

        service = PokemonApiService()
        pokemon_data = service.get_pokemon_details(name)

        if not pokemon_data:
            raise ValidationError({"error": f"Pokemon with name '{name}' not found."})

        serializer.save(
            pokemon_id=pokemon_data.get('id'),
            name=pokemon_data.get('name'),
            types=pokemon_data.get('types'),
            abilities=pokemon_data.get('abilities'),
            base_stats=pokemon_data.get('stats'),
            height=pokemon_data.get('height'),
            weight=pokemon_data.get('weight'),
            image_url=pokemon_data.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default'),
        )


class PokemonUpdateView(UpdateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Pokemon, name=name)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        non_modifiable_fields = ['pokemon_id', 'name', 'created_at', 'updated_at']
        data = {key: value for key, value in request.data.items() if key not in non_modifiable_fields}

        if not data:
            return Response({"error": "It's not an updatable field."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(data=serializer.data)


class PokemonDeleteView(DestroyAPIView):
    queryset = Pokemon.objects.all()

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Pokemon, name=name)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": f"Pokemon '{instance.name}' deleted successfully."}, status=status.HTTP_200_OK)


class PokemonRetrieveView(RetrieveAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(Pokemon, name=name)


class PokemonListView(ListAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


class PokemonScoreView(APIView):
    def get(self, request):
        score_service = ScoreService()
        pokemons = Pokemon.objects.all()
        scores = []
        for pokemon in pokemons:
            pokemon_data = {
                'types': pokemon.types,
                'base_stats': pokemon.base_stats,
                'abilities': pokemon.abilities,
                'height': pokemon.height,
                'weight': pokemon.weight,
            }
            score = score_service.calculate_score(pokemon_data)
            scores.append({
                'name': pokemon.name,
                'score': score
            })

        return Response(scores, status=status.HTTP_200_OK)
