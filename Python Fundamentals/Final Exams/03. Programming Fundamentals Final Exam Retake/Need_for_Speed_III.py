def drive(garage, car, distance, fuel):
    if garage[car]['fuel'] < fuel:
        return "Not enough fuel to make that ride"
    else:
        garage[car]['mileage'] += distance
        garage[car]['fuel'] -= fuel
        return f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."


def refuel(garage, car, fuel):
    if garage[car]['fuel'] + fuel <= 75:
        garage[car]['fuel'] += fuel
        return f"{car} refueled with {fuel} liters"
    refilled_fuel = 75 - garage[car]['fuel']
    garage[car]['fuel'] = 75
    return f"{car} refueled with {refilled_fuel} liters"


n = int(input())
garage = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    garage[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while not command == "Stop":
    command_data = command.split(" : ")
    action = command_data[0]
    car = command_data[1]
    if action == "Drive":
        distance = int(command_data[2])
        fuel = int(command_data[3])
        print(drive(garage, car, distance, fuel))
        if garage[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            garage.pop(car)
    elif action == "Refuel":
        fuel = int(command_data[2])
        print(refuel(garage, car, fuel))
    elif action == "Revert":
        kilometers = int(command_data[2])
        if garage[car]['mileage'] - kilometers >= 10000:
            garage[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            garage[car]['mileage'] = 10000
    command = input()

for car, info in sorted(garage.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0])):
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
