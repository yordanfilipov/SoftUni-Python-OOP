from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")

    def calculate_comfort(self):
        sum_comfort = sum([c.comfort for c in self.decorations])
        return sum_comfort

    def add_fish(self, fish):
        if self.capacity > 0:
            self.fish.append(fish)
            self.capacity -= 1
            return f'Successfully added {fish.__class__.name} to {self.name}.'
        else:
            return 'Not enough capacity.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)
            self.capacity += 1

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = ''
        if len(self.fish) > 0:
            result += f"{self.name}:\nFish: {' '.join([el.name for el in self.fish])}\n" \
                      f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        else:
            result += f"{self.name}:\nFish: {'none'}\n" \
                      f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort}"
        return result