from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    _COST = 15
    _MEMBERS_COUNT = 2
    _APPLIANCES = [TV(), Fridge(), Stove()]

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, OldCouple._MEMBERS_COUNT)
        self.room_cost = OldCouple._COST
        self.appliances = OldCouple._APPLIANCES * OldCouple._MEMBERS_COUNT

        self.calculate_expenses(self.appliances)
