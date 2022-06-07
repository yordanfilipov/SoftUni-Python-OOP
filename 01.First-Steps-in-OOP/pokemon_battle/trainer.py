from pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon):
        for p in self.pokemon:
            if p.name == pokemon:
                self.pokemon.remove(p)
                return f"You have released {pokemon}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            result += f"- {p.pokemon_details()}" + "\n"
        return result