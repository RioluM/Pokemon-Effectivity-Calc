import requests
from models.type import Type
from models.attack import Attack
from models.pokemon import Pokemon


class DataParser:
    def get_type(self, type_name):
        type_data = requests.get(f"https://pokeapi.co/api/v2/type/{type_name}")
        return Type(type_name, type_data.json()["damage_relations"])

    def get_input_results(self):
        types_input = input()
        types_list = types_input.split(" ")
        types_list.pop(1)
        types = {type_name: self.get_type(type_name) for type_name in set(types_list)}
        attack_type = types[types_list[0]]
        pokemon_types = [types[type_name] for type_name in types_list[1:]]
        return Attack(attack_type), Pokemon(pokemon_types)
