from collections import deque

petrol_pumps_count = int(input())

pumps = deque()

for pump in range(petrol_pumps_count):
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])

for i in range(len(pumps)):
    fuel_tank = 0
    successful_pumps = 0
    for pump in pumps:
        fuel = pump[0]
        distance = pump[1]
        fuel_tank += fuel
        if fuel_tank - distance < 0:
            break
        fuel_tank -= distance
        successful_pumps += 1
    if successful_pumps == petrol_pumps_count:
        print(i)
        break
    else:
        pumps.rotate(-1)
