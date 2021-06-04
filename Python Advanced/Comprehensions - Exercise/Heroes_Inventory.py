heroes_names = input().split(', ')

heroes_inventories = {hero: {} for hero in heroes_names}

command = input()
while not command == "End":
    hero, item, cost = command.split('-')
    cost = int(cost)
    if item not in heroes_inventories[hero]:
        heroes_inventories[hero][item] = int(cost)
    command = input()

for hero in heroes_names:
    print(f"{hero} -> Items: {len(heroes_inventories[hero])}, Cost: {sum(heroes_inventories[hero].values())}")
