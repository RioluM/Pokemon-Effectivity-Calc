from json.decoder import JSONDecodeError
from data_parser import DataParser


data_parser = DataParser()
try:
    attack, pokemon = data_parser.get_input_results()
except (JSONDecodeError, KeyError) as e:
    print("Invalid input data")
    exit()

attack_effect = 1
for pokemon_type in pokemon.types:
    if attack.type.name in pokemon_type.double_damage_from:
        attack_effect *= 2
        continue
    if attack.type.name in pokemon_type.half_damage_from:
        attack_effect *= 0.5
        continue
    if attack.type.name in pokemon_type.no_damage_from:
        attack_effect *= 0
        continue
print(f"{attack_effect}x")
