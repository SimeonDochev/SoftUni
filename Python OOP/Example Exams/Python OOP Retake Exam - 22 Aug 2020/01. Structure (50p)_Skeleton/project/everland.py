from project.rooms.room import Room


class Everland:
    _DAYS_IN_MONTH = 30

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = sum([r.expenses + r._COST for r in self.rooms])
        return f"Monthly consumption: {consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            room_cost = room.expenses + room._COST
            if room.budget >= room_cost:
                result.append(f"{room.family_name} paid {room_cost:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= room_cost
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])
        result = f"Total population: {total_population}\n"
        for room in self.rooms:
            room.calculate_expenses(room.appliances, room.children)
            result += f"{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget:.2f}$, " \
                      f"Expenses: {room.expenses:.2f}$\n"
            if room.children:
                n = 1
                for child in room.children:
                    result += f"--- Child {n} monthly cost: {child.cost*Everland._DAYS_IN_MONTH:.2f}$\n"
                    n += 1
            result += f"--- Appliances monthly cost: {sum(ap.get_monthly_expense() for ap in room.appliances):.2f}$\n"

        return result
