from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)
        self.name = name
        self.species = species
        self.price = price

    def eat(self):
        self.size += 2