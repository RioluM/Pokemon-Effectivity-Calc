

class Type:
    def __init__(self, name, damage_relations):
        self.name = name
        self.double_damage_from = [double_damage["name"] for double_damage in damage_relations['double_damage_from']]
        self.half_damage_from = [half_damage["name"] for half_damage in damage_relations['half_damage_from']]
        self.no_damage_from = [no_damage["name"] for no_damage in damage_relations['no_damage_from']]
