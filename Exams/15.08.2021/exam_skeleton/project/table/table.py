from abc import ABC, abstractmethod


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        if not self.is_reserved:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = sum([f.price for f in self.food_orders])
        drink_bill = sum([d.price for d in self.drink_orders])
        bill = food_bill + drink_bill
        return bill

    def clear(self):
        self.drink_orders = []
        self.food_orders = []
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            string_to_return = f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
            return string_to_return
