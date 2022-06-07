from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    comfort_count = 5
    initial_price = 10

    def __init__(self):
        super().__init__(self.comfort_count, self.initial_price)