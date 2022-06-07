from appliances.fridge import Fridge
from appliances.laptop import Laptop
from appliances.tv import TV
from rooms.room import Room


class YoungCoupleWithChildren(Room):
    initial_room_members_count = 2
    room_cost = 30

    def __init__(self, family_name, salary_one, salary_two, *children):
        members_count = self.initial_room_members_count + len(children)
        super().__init__(family_name, salary_one + salary_two, members_count)
        self.children = list(children)
        self.appliances = self.__generate_appliances()
        self.calculate_expenses(self.appliances, self.children)

    def __generate_appliances(self):
        appliances = []
        for x in range(self.members_count):
            appliances.append(TV())
            appliances.append(Fridge())
            appliances.append(Laptop())
        return appliances