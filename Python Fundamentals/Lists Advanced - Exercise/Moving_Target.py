def shoot(targets, index, power):
    targets[index] -= power
    if targets[index] <= 0:
        targets.pop(index)


def add(targets, index, value):
    targets.insert(index, value)


def strike(targets, index, radius):
    stroke_targets = targets[index-radius:index] + targets[index:index+(radius+1)]
    for tar in stroke_targets:
        targets.remove(tar)


targets_list = list(map(lambda x: int(x), input().split()))

command = input()
while not command == "End":
    command_data = command.split()
    target_index = int(command_data[1])
    if command_data[0] == "Shoot":
        shot_power = int(command_data[2])
        if 0 <= target_index < len(targets_list):
            shoot(targets_list, target_index, shot_power)
    elif command_data[0] == "Add":
        command_value = int(command_data[2])
        if 0 <= target_index < len(targets_list):
            add(targets_list, target_index, command_value)
        else:
            print("Invalid placement!")
    elif command_data[0] == "Strike":
        strike_radius = int(command_data[2])
        if not target_index - strike_radius < 0 and not target_index + strike_radius >= len(targets_list):
            strike(targets_list, target_index, strike_radius)
        else:
            print("Strike missed!")
    command = input()

final_targets_list = list(map(lambda x: str(x), targets_list))
print("|".join(final_targets_list))
