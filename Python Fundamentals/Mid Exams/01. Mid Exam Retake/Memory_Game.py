elements_list = input().split()

moves_count = 1

command = input()
while not command == "end":
    first_index, second_index = map(int, command.split())
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index > len(elements_list)-1 or second_index > len(elements_list)-1:
        print("Invalid input! Adding additional elements to the board")
        half = int(len(elements_list) / 2)
        elements_list.insert(half, f"-{moves_count}a")
        elements_list.insert(half, f"-{moves_count}a")
        command = input()
        continue
    if elements_list[first_index] == elements_list[second_index]:
        element = elements_list[0]
        print(f"Congrats! You have found matching elements - {element}!")
        elements_list.remove(element)
        elements_list.remove(element)
    elif not elements_list[first_index] == elements_list[second_index]:
        print("Try again!")
    if not elements_list:
        print(f"You have won in {moves_count} turns!")
        break
    moves_count += 1
    command = input()

if command == "end":
    print(f"Sorry you lose :(\n{' '.join(elements_list)}")


