n = int(input())

plants_data = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants_data[plant] = [int(rarity)]

command = input()
while not command == "Exhibition":
    if ":" in command:
        command_data = command.split(":")
        action = command_data[0]
        action_data = command_data[1].split(" - ")
        plant = action_data[0].strip()
        if plant not in plants_data:
            print("error")
            command = input()
            continue
        if action == "Rate":
            rating = int(action_data[1].strip())
            if plant in plants_data:
                plants_data[plant].append(rating)
        elif action == "Update":
            new_rarity = int(action_data[1].strip())
            if plant in plants_data:
                plants_data[plant][0] = new_rarity
        elif action == "Reset":
            if plant in plants_data:
                plants_data[plant] = plants_data[plant][:1]
        else:
            print("error")
        command = input()
    else:
        print("error")
        command = input()

for plant in plants_data:
    ratings_count = len(plants_data[plant][1::])
    if not ratings_count == 0:
        plants_data[plant] = [plants_data[plant][0], sum(plants_data[plant][1::]) / ratings_count]
    else:
        plants_data[plant] = [plants_data[plant][0], 0]

print("Plants for the exhibition:")
for k, v in sorted(plants_data.items(), key=lambda kvp: (-kvp[1][0], -kvp[1][1])):
    print(f"- {k}; Rarity: {v[0]}; Rating: {v[1]:.2f}")
