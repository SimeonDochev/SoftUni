from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    _COST = 10
    _MEMBERS_COUNT = 1
    _APPLIANCES = [TV()]

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, AloneYoung._MEMBERS_COUNT)
        self.room_cost = AloneYoung._COST
        self.appliances = AloneYoung._APPLIANCES

        self.calculate_expenses(self.appliances)
