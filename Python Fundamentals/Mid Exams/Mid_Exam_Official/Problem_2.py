def move_left(array, i):
    array.insert(i - 1, array.pop(i))


def move_right(array, i):
    array.insert(i + 1, array.pop(i))


def check_even(array):
    result = ""
    for i in range(len(array)):
        if i % 2 == 0:
            result += f"{array[i]} "
    return result


def check_odd(array):
    result = ""
    for i in range(len(array)):
        if not i % 2 == 0:
            result += f"{array[i]} "
    return result


particles = input().split("|")

command = input()
while not command == "Done":
    command_data = command.split()
    action = command_data[0]
    if action == "Move":
        direction = command_data[1]
        index = int(command_data[2])
        if direction == "Left":
            if not index <= 0 and not index > len(particles) - 1:
                move_left(particles, index)
        elif direction == "Right":
            if not index < 0 and not index >= len(particles) - 1:
                move_right(particles, index)
    elif action == "Check":
        even_or_odd = command_data[1]
        if even_or_odd == "Even":
            print(check_even(particles))
        elif even_or_odd == "Odd":
            print(check_odd(particles))
    command = input()

weapon_name = "".join(particles)
print(f"You crafted {weapon_name}!")
