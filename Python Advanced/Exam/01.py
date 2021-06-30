from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cups_of_milk = deque([int(el) for el in input().split(', ')])

chocolate_milkshakes = 0

while chocolate_milkshakes < 5:
    if not chocolates or not cups_of_milk:
        break

    current_chocolate = chocolates[-1]
    current_cup = cups_of_milk[0]

    if current_chocolate <= 0 or current_cup <= 0:
        if current_chocolate <= 0:
            chocolates.pop()
        if current_cup <= 0:
            cups_of_milk.popleft()
        continue

    if chocolates.pop() - cups_of_milk.popleft() == 0:
        chocolate_milkshakes += 1
    else:
        cups_of_milk.append(current_cup)
        current_chocolate -= 5
        chocolates.append(current_chocolate)

if chocolate_milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print("Milk: empty")
