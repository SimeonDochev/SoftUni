from collections import deque

liters = int(input())

name = input()
queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        liters += int(command.split()[-1])
    else:
        current_person = queue.popleft()
        liters_needed = int(command)
        if liters_needed <= liters:
            print(f"{current_person} got water")
            liters -= liters_needed
        else:
            print(f"{current_person} must wait")
    command = input()

print(f"{liters} liters left")