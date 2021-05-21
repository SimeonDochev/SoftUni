energy = 100
coins = 100

events_list = input().split("|")
flag = True

for event in range(len(events_list)):
    current_event_info = events_list[event].split("-")
    current_event_command = current_event_info[0]
    current_event_digit = int(current_event_info[1])
    if current_event_command == "rest":
        energy += current_event_digit
        if energy <= 100:
            print(f"You gained {current_event_digit} energy.")
        else:
            excess_energy = energy - 100
            print(f"You gained {current_event_digit - excess_energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")
    elif current_event_command == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += current_event_digit
            print(f"You earned {current_event_digit} coins.")
    else:
        coins -= current_event_digit
        if coins > 0:
            print(f"You bought {current_event_command}.")
        else:
            print(f"Closed! Cannot afford {current_event_command}.")
            flag = False
            break

if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
