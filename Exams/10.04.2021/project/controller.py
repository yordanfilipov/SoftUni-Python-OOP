from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        elif aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        else:
            return 'Invalid aquarium type.'

    def add_decoration(self, decoration_type):
        if decoration_type == "Ornament":
            self.decorations_repository.decorations.append(Ornament())
            return f'Successfully added {decoration_type}.'
        elif decoration_type == 'Plant':
            self.decorations_repository.decorations.append(Plant())
            return f'Successfully added {decoration_type}.'
        else:
            return 'Invalid decoration type.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        try:
            decoration = \
                [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type][0]
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

        try:
            aquarium = \
                [a for a in self.aquariums if a.name == aquarium_name][0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        except IndexError:
            return

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type != "FreshwaterFish" or fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."
        else:
            if fish_type == "FreshwaterFish":
                fish = FreshwaterFish(fish_name, fish_species, price)
            else:
                fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            if "Freshwater" in aquarium.__class__.__name__ and "Freshwater" in fish.__class__.__name__:
                return aquarium.add_fish(fish)
            elif "Saltwater" in aquarium.__class__.__name__ and "Saltwater" in fish.__class__.__name__:
                return aquarium.add_fish(fish)
            else:
                return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        value_fish = sum([f.price for f in aquarium.fish])
        value_decorations = sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {(value_fish + value_decorations):.2f}."

    def report(self):
        result = "\n".join([str(a) for a in self.aquariums])
        return result
