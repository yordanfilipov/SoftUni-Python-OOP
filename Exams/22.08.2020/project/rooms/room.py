class Room:
    room_cost = 0

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            result += sum(x.get_monthly_expense() for x in items)
        self.expenses = result
        return result


    @staticmethod
    def __validate_expenses(value):
        if value and value < 0:
            raise ValueError("Expenses cannot be negative")

    def __repr__(self):
        consumers_result = self.get_consumer_results()
        result = [
            f'{self.family_name} with {self.members_count} members. Budget: {self.budget}$, Expenses: {self.expenses}$'
        ]