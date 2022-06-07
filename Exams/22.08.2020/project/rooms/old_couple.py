from appliances.fridge import Fridge
from appliances.stove import Stove
from appliances.tv import TV
from rooms.room import Room


class OldCouple(Room):
    default_room_members_count = 2
    room_cost = 15
    appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, self.default_room_members_count)
        self.calculate_expenses(self.appliances)