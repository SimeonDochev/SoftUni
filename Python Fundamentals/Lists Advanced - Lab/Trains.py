def add_people_to_last_wagon(wagons, people_count):
    wagons[-1] += people_count


def add_people_to_wagon(wagons, wagon, people_count):
    wagons[wagon] += people_count


def remove_people_from_wagon(wagons, wagon, people_count):
    wagons[wagon] -= people_count


wagons_count = int(input())
wagons_list = [0] * wagons_count

command = input()
while not command == "End":
    command_data = command.split()
    action = command_data[0]
    if action == "add":
        people = int(command_data[1])
        add_people_to_last_wagon(wagons_list, people)
    elif action == "insert":
        people = int(command_data[2])
        wagon_index = int(command_data[1])
        add_people_to_wagon(wagons_list, wagon_index, people)
    elif action == "leave":
        people = int(command_data[2])
        wagon_index = int(command_data[1])
        remove_people_from_wagon(wagons_list, wagon_index, people)
    command = input()

print(wagons_list)