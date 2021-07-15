from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number]
        if room:
            searched_room = room[0]
            result = searched_room.take_room(people)
            if not result:
                self.guests += people

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number and room.is_taken]
        if room:
            searched_room = room[0]
            self.guests -= searched_room.guests
            searched_room.free_room()

    def status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"
