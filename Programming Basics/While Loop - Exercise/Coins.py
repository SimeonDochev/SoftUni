change = float(input())
counter = 0

while change > 0:
    if change - 2 >= 0:
        change = round(change - 2, 2)
        counter += 1
    elif change - 1 >= 0:
        change = round(change - 1, 2)
        counter += 1
    elif change - 0.5 >= 0:
        change = round(change - 0.5, 2)
        counter += 1
    elif change - 0.2 >= 0:
        change = round(change - 0.2, 2)
        counter += 1
    elif change - 0.1 >= 0:
        change = round(change - 0.1, 2)
        counter += 1
    elif change - 0.05 >= 0:
        change = round(change - 0.05, 2)
        counter += 1
    elif change - 0.02 >= 0:
        change = round(change - 0.02, 2)
        counter += 1
    elif change - 0.01 >= 0:
        change = round(change - 0.01, 2)
        counter += 1

print(f'{counter:.0f}')
