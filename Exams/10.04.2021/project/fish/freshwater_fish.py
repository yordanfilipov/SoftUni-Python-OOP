from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)
        self.name = name
        self.species = species
        self.price = price

    def eat(self):
        self.size += 3