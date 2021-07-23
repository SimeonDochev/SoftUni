class Room:
    _DAYS_IN_MONTH = 30

    def __init__(self, family_name, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for li in args:
            result += sum([el.cost for el in li])
        self.expenses = result * Room._DAYS_IN_MONTH
