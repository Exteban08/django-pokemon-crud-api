from typing import Dict, Optional, Any

import requests


class PokemonApiService:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://pokeapi.co/api/v2"

    def get_pokemon_details(self, pokemon_name: str) -> Optional[Dict[str, Any]]:
        print(f"Fetching details for {pokemon_name}")

        try:
            response = self.session.get(f"{self.base_url}/pokemon/{pokemon_name.lower()}")
            response.raise_for_status()
            data = response.json()

            return data
        except requests.RequestException:
            return None

    # def search_pokemon(self, query: str) -> List[Dict[str, Any]]:
    #     try:
    #         pokemon_data = self.get_pokemon_details(query.lower())
    #         if pokemon_data:
    #             return [pokemon_data]
    #
    #         response = self.session.get(f"{self.base_url}/pokemon?limit=1000")
    #         response.raise_for_status()
    #
    #         all_pokemon = response.json().get('results', [])
    #         filtered_pokemon = [
    #             pokemon for pokemon in all_pokemon
    #             if query.lower() in pokemon['name']
    #         ]
    #
    #         result = []
    #         for pokemon in filtered_pokemon[:10]:
    #             details = self.get_pokemon_details(pokemon['name'])
    #             if details:
    #                 result.append(details)
    #
    #         return result
    #     except requests.RequestException:
    #         return []
    #
    # def _transform_pokemon_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
    #     types = [type_info['type']['name'] for type_info in data.get('types', [])]
    #
    #     abilities = [ability_info['ability']['name'] for ability_info in data.get('abilities', [])]
    #
    #     stats = {}
    #     for stat_info in data.get('stats', []):
    #         stat_name = stat_info['stat']['name']
    #         stat_value = stat_info['base_stat']
    #         stats[stat_name] = stat_value
    #
    #     image_url = data['sprites']['other']['official-artwork']['front_default']
    #     if not image_url:
    #         image_url = data['sprites']['front_default']
    #
    #     return {
    #         'pokemon_id': data.get('id'),
    #         'name': data.get('name'),
    #         'types': types,
    #         'abilities': abilities,
    #         'base_stats': stats,
    #         'height': data.get('height', 0) / 10,
    #         'weight': data.get('weight', 0) / 10,
    #         'image_url': image_url
    #     }
    #
    # def fetch_all_pokemons(self, limit: int = 25) -> List[Dict[str, Any]]:
    #     try:
    #         response = requests.get(f"{self.base_url}/pokemon?limit={limit}")
    #         response.raise_for_status()
    #         all_pokemon = response.json()['results']
    #
    #         detailed_pokemon = []
    #         for pokemon in all_pokemon:
    #             pokemon_data = self.get_pokemon_details(pokemon['name'])
    #             if pokemon_data:
    #                 detailed_pokemon.append(pokemon_data)
    #
    #         return detailed_pokemon
    #     except requests.RequestException:
    #         return []
    #
    #
    # def fetch_pokemons_by_type(self, type_: str) -> List[Dict[str, Any]]:
    #     try:
    #         response = self.session.get(f"{self.base_url}/type/{type_.lower()}")
    #         response.raise_for_status()
    #         data = response.json()
    #
    #         pokemon_entries = data.get('pokemon', [])
    #         pokemon_names = [entry['pokemon']['name'] for entry in pokemon_entries]
    #
    #         detailed_pokemons = []
    #         for name in pokemon_names:
    #             details = self.get_pokemon_details(name)
    #             if details:
    #                 detailed_pokemons.append(details)
    #
    #         return detailed_pokemons
    #     except requests.RequestException:
    #         return []
