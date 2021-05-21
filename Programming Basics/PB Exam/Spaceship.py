from math import floor
width = float(input())
length = float(input())
height = float(input())
average_height = float(input())
volume = width * length * height
room_volume = (average_height + 0.4) * 2 * 2
people = floor(volume / room_volume)

if people < 3:
    print('The spacecraft is too small.')
elif people > 10:
    print(f'The spacecraft is too big.')
else:
    print(f'The spacecraft holds {people} astronauts.')
