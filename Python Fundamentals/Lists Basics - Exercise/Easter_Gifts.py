gifts_as_list = input().split()

command = input()

while not command == "No Money":
    current_command = command.split()
    if current_command[0] == "OutOfStock":
        if current_command[1] in gifts_as_list:
            for gift in range(len(gifts_as_list)):
                if gifts_as_list[gift] == current_command[1]:
                    gifts_as_list[gift] = "None"
    elif current_command[0] == "Required":
        if 0 <= int(current_command[2]) < len(gifts_as_list):
            gifts_as_list[int(current_command[2])] = current_command[1]
    elif current_command[0] == "JustInCase":
        gifts_as_list[-1] = current_command[1]
    command = input()

for gift in gifts_as_list:
    if not gift == "None":
        print(gift, end=" ")
