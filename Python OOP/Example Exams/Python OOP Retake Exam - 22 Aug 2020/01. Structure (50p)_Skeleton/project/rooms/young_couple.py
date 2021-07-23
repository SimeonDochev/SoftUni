from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    _COST = 20
    _MEMBERS_COUNT = 2
    _APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, YoungCouple._MEMBERS_COUNT)
        self.room_cost = YoungCouple._COST
        self.appliances = YoungCouple._APPLIANCES * YoungCouple._MEMBERS_COUNT

        self.calculate_expenses(self.appliances)
