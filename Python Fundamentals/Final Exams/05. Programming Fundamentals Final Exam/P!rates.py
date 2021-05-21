def plunder(towns, town, people, gold):
    towns[town]['population'] -= people
    towns[town]['gold'] -= gold
    if towns[town]['population'] <= 0 or towns[town]['gold'] <= 0:
        towns.pop(town)
        return f"{town} plundered! {gold} gold stolen, {people} citizens killed.\n{town} has been wiped off the map!"
    return f"{town} plundered! {gold} gold stolen, {people} citizens killed."


def prosper(towns, town, gold):
    if gold < 0:
        return "Gold added cannot be a negative number!"
    towns[town]['gold'] += gold
    return f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold."


towns = {}

command = input()
while not command == "Sail":
    town_name, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if town_name not in towns:
        towns[town_name] = {'population': population, 'gold': gold}
    else:
        towns[town_name]['population'] += population
        towns[town_name]['gold'] += gold
    command = input()

command = input()
while not command == "End":
    command_data = command.split("=>")
    action = command_data[0]
    town = command_data[1]
    if action == "Plunder":
        people = int(command_data[2])
        gold = int(command_data[3])
        print(plunder(towns, town, people, gold))
    elif action == "Prosper":
        gold = int(command_data[2])
        print(prosper(towns, town, gold))
    command = input()

print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
for town, info in sorted(towns.items(), key=lambda kvp: (-kvp[1]['gold'], kvp[0])):
    print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
