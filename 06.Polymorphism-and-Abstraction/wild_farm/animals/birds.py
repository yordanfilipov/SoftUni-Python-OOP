from animals.animal import Bird
from food import Meat, Vegetable, Fruit, Food, Seed


class Owl(Bird):

    allowed_food = [Meat]
    gained_weight = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if type(food) not in self.allowed_food:
    #         return f"Owl does not eat {type(food).__name__}!"
    #     self.weight += food.quantity * 0.25
    #     self.food_eaten += food.quantity
    #
    # def __repr__(self):
    #     return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):

    allowed_food = [Vegetable, Fruit, Food, Meat, Seed]
    gained_weight = 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     if type(food) not in self.allowed_food:
    #         return f"Hen does not eat {type(food).__name__}!"
    #     self.weight += food.quantity * 0.35
    #     self.food_eaten += food.quantity


