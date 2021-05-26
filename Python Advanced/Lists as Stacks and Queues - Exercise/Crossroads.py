from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars_que = deque()
crash = False
total_safe_cars = 0

command = input()
while not command == "END":
    if not command == "green":
        cars_que.append(command)
    else:
        total_duration = green_light_duration + free_window_duration
        current_car = cars_que.popleft()
        chars = deque(current_car)
        if total_duration - free_window_duration > 0:
            while chars:
                current_car = chars.popleft()

    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{total_safe_cars} total cars passed the crossroads.")
