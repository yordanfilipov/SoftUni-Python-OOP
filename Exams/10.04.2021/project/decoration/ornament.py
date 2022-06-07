from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    comfort_count = 1
    initial_price = 5

    def __init__(self):
        super().__init__(self.comfort_count, self.initial_price)
