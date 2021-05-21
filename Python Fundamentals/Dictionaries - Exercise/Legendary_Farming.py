inventory = {"motes": 0, "fragments": 0, "shards": 0}

is_accomplished = False

while not is_accomplished:
    materials = input().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        item = materials[i + 1].lower()
        if item not in inventory:
            inventory[item] = 0
        inventory[item] += quantity
        if item == "motes":
            if inventory["motes"] >= 250:
                is_accomplished = True
                break
        elif item == "fragments":
            if inventory["fragments"] >= 250:
                is_accomplished = True
                break
        elif item == "shards":
            if inventory["shards"] >= 250:
                is_accomplished = True
                break
    if is_accomplished:
        break

if inventory["motes"] >= 250:
    inventory["motes"] -= 250
    print("Dragonwrath obtained!")
elif inventory["fragments"] >= 250:
    inventory["fragments"] -= 250
    print("Valanyr obtained!")
elif inventory["shards"] >= 250:
    inventory["shards"] -= 250
    print("Shadowmourne obtained!")

for item, quantity in sorted(inventory.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    if item == "motes" or item == "shards" or item == "fragments":
        print(f"{item}: {quantity}")
for item, quantity in sorted(inventory.items(), key=lambda kvp: kvp[0]):
    if not item == "motes" and not item == "shards" and not item == "fragments":
        print(f"{item}: {quantity}")
