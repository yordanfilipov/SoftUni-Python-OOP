from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        food = [f.name for f in self.food_menu]
        if name in food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            food_to_add = Bread(name, price)
        else:
            food_to_add = Cake(name, price)
        self.food_menu.append(food_to_add)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = [d.name for d in self.drinks_menu]
        if name in drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Water":
            drink_to_add = Water(name, portion, brand)
        else:
            drink_to_add = Tea(name, portion, brand)
        self.drinks_menu.append(drink_to_add)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        tables = [t.table_number for t in self.tables_repository]
        if table_number in tables:
            raise Exception(f'Table {table_number} is already in the bakery!')
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        else:
            table = OutsideTable(table_number, capacity)
        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    # def reserve_table(self, number_of_people):
    #     free_table = [t for t in self.tables_repository
    #                   if t.is_reserved is False and t.capacity >= number_of_people]
    #     if free_table:
    #         free_table = free_table[0]
    #         free_table.is_reserved = True
    #         return f'Table {free_table.table_number} has been reserved for {number_of_people} people'
    #     else:
    #         return f'No available table for {number_of_people} people'

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.reserve(number_of_people)
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        food_not_in_menu = []
        for food in args:
            order = [f for f in self.food_menu if f.name == food]
            if not order:
                food_not_in_menu.append(food)
            else:
                table.order_food(order[0])
        string_to_return = f"Table {table_number} ordered:\n"
        for food in table.food_orders:
            string_to_return += f"{repr(food)}\n"
        string_to_return += f"{self.name} does not have in the menu:\n"
        for food in food_not_in_menu:
            string_to_return += f"{food}\n"
        return string_to_return

    def order_drink(self, table_number, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        table = table[0]
        drink_not_in_menu = []
        for drink in args:
            order = [d for d in self.drinks_menu if d.name == drink]
            if not order:
                drink_not_in_menu.append(drink)
            else:
                table.order_drink(order[0])
        string_to_return = f"Table {table_number} ordered:\n"
        for drink in table.drink_orders:
            string_to_return += f"{repr(drink)}\n"
        string_to_return += f"{self.name} does not have in the menu:\n"
        for drink in drink_not_in_menu:
            string_to_return += f"{drink}\n"
        return string_to_return

    # def leave_table(self, table_number):
    #     for table in self.tables_repository:
    #         if table.table_number == table_number:
    #             bill = table.get_bill()
    #             table.clear()
    #             self.total_income += bill
    #             result = f'"Table: {table_number}"\n"Bill: {bill:.2f}"'
    #             return result

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        bill = 0
        if table:
            table = table[0]
            bill = table.get_bill()
            table.clear()
            self.total_income += bill
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        res = ""
        for table in self.tables_repository:
            if table.is_reserved:
                res += f'\n{table.free_table_info()}'
        return res

    def get_total_income(self):
        return f'"Total income: {self.total_income:.2f}lv"'

# def ads(dsf, *args):
#     dsf = dsf
#     ll = list(args)
#     print(ll)
#
# ads("asd", 1, 2, 3, 4, 5)
