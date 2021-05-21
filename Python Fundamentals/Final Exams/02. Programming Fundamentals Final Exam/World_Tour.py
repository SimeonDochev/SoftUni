stops = input()

command = input()
while not command == "Travel":
    command_data = command.split(":")
    if command_data[0] == "Add Stop":
        index = int(command_data[1])
        string = command_data[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif command_data[0] == "Remove Stop":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
    elif command_data[0] == "Switch":
        old_string = command_data[1]
        new_string = command_data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
