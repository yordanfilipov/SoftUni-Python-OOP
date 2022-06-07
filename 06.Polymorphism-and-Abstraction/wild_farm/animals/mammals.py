from animals.animal import Mammal
from food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    allowed_food = [Vegetable, Fruit]
    gained_weight = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    allowed_food = [Meat]
    gained_weight = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):

    allowed_food = [Vegetable, Meat]
    gained_weight = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):

    allowed_food = [Meat]
    gained_weight = 1

    def make_sound(self):
        return "ROAR!!!"
