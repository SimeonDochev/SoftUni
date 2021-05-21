from math import ceil

speed = float(input())
fuel = float(input())

distance = 384_400 * 2
total_time = ceil(distance / speed) + 3
total_fuel = fuel * distance / 100

print(total_time)
print(f'{total_fuel:.0f}')