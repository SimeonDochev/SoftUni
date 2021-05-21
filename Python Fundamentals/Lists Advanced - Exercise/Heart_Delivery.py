neighbourhood_hearts_needed = list(map(lambda x: int(x), input().split("@")))

current_position = 0
command = input()
while not command == "Love!":
    command_data = command.split()
    jump_length = int(command_data[1])
    current_position += jump_length
    if current_position >= len(neighbourhood_hearts_needed):
        current_position = 0
    if neighbourhood_hearts_needed[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
        command = input()
        continue
    neighbourhood_hearts_needed[current_position] -= 2
    if neighbourhood_hearts_needed[current_position] == 0:
        print(f"Place {current_position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_position}.")
if sum(neighbourhood_hearts_needed) == 0:
    print("Mission was successful.")
else:
    failed_houses = list(filter(lambda x: x > 0, neighbourhood_hearts_needed))
    print(f"Cupid has failed {len(failed_houses)} places.")
