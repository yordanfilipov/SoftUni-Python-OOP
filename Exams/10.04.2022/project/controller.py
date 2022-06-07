from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        players = list(args)
        added_players = []
        for pl in players:
            if pl not in self.players:
                self.players.append(pl)
                added_players.append(pl.name)
        result = f'Successfully added: {", ".join(added_players)}'
        return result

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player = [p for p in self.players if p.name == player_name][0]
        if sustenance_type == "Food" or sustenance_type == "Drink" or player:
            is_food = [f for f in self.supplies if f.__class__.__name__ == "Food"]
            is_drink = [d for d in self.supplies if d.__class__.__name__ == "Drink"]
            if not is_food:
                raise Exception("There are no food supplies left!")
            if not is_drink:
                raise Exception("There are no drink supplies left!")
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."
            self.supplies.reverse()
            for sup in self.supplies:
                if sup.name == sustenance_type:
                    energy = sup.energy
                    self.supplies.remove(sup)
                    self.supplies.reverse()
                    player.stamina += energy
                    if player.stamina > 100:
                        player.stamina = 100
                    return f"{player_name} sustained successfully with {sup.name}."

    # def duel(self, first_player_name, second_player_name):
    #     if first_player.stamina == 0 and second_player.stamina == 0:
    #         return f'Player {first_player_name} does not have enough stamina.\n' \
    #                f'Player {second_player_name} does not have enough stamina.'
    #     if first_player.stamina == 0:
    #         return f'Player {first_player_name} does not have enough stamina.'
    #     if second_player.stamina == 0:
    #         return f'Player {second_player_name} does not have enough stamina.'
    #     if first_player.stamina > second_player.stamina:
    #         second_player.stamina -= first_player.stamina / 2
    #     else:
    #         first_player.stamina -= second_player.stamina / 2
    #     first_player = [f for f in self.players if f.name == first_player_name][0]
    #     second_player = [s for s in self.players if s.name == second_player_name][0]
    #     first_player.is_stamina_equals_zero()
    #     second_player.is_stamina_equals_zero()
    #     if first_player.is_stamina_zero or second_player.is_stamina_zero:
    #         return f'Player {first_player.name} does not have enough stamina.\n' \
    #                f'Player {second_player.name} does not have enough stamina.'
    #     if first_player.stamina < second_player.stamina:
    #         self.attack(second_player, first_player)
    #         self.attack(first_player, second_player)
    #     else:
    #         self.attack(first_player, second_player)
    #         self.attack(first_player, second_player)

    # def is_stamina_equals_zero(self, player):
    #     if player.stamina == 0:
    #         player.is_stamina_zero = True
    #         return f'Player {player.name} does not have enough stamina.\n'
    #
    # def attack(self, player_one, player_two):
    #     player_one.stamina -= player_two.stamina / 2
    #     return

    def next_day(self):
        pass

    def __str__(self):
        pass


# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
