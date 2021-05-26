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
        total_time = green_light_duration + free_window_duration
        while cars_que and not total_time <= free_window_duration:
            current_car = cars_que.popleft()
            chars = deque(current_car)
            while chars:
                current_char = chars.popleft()
                total_time -= 1
                if total_time < 0:
                    crash = True
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_char}.")
                    break
            total_safe_cars += 1
            if crash:
                break
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{total_safe_cars} total cars passed the crossroads.")
