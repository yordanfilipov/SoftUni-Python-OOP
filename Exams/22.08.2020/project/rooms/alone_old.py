from rooms.room import Room


class AloneOld(Room):
    default_room_members_count = 1
    room_cost = 10

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, self.default_room_members_count)
