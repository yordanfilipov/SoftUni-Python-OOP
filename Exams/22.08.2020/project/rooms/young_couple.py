from appliances.fridge import Fridge
from appliances.laptop import Laptop
from appliances.tv import TV
from rooms.room import Room


class YoungCouple(Room):
    default_room_members_count = 2
    room_cost = 20
    appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, self.default_room_members_count)
        self.calculate_expenses(self.appliances)