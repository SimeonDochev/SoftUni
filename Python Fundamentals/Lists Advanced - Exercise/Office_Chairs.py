rooms_count = int(input())
chairs_needed = []
free_chairs = []

for room in range(rooms_count):
    current_room_info = input().split()
    current_room_chairs = len(current_room_info[0])
    current_room_people = int(current_room_info[1])
    if current_room_chairs < current_room_people:
        lack = abs(current_room_chairs - current_room_people)
        chairs_needed.append(lack)
        free_chairs.append(0)
    else:
        chairs_needed.append(0)
        free_chairs.append(current_room_chairs - current_room_people)

if sum(chairs_needed) == 0:
    print(f"Game On, {sum(free_chairs)} free chairs left")
else:
    for i in range(len(chairs_needed)):
        if chairs_needed[i] == 0:
            continue
        else:
            print(f"{chairs_needed[i]} more chairs needed in room {i+1}")
