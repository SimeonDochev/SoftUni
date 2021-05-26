from collections import deque

robots = input().split(";")
robots_info = {}

for robot in robots:
    name, process_time = robot.split("-")
    process_time = int(process_time)
    robots_info[name] = {"process_time": process_time, "availability": True, "time_until_available": process_time}

hh, mm, ss = map(int, input().split(":"))

products = deque()
product = input()
while not product == "End":
    products.append(product)
    product = input()

while products:
    ss += 1
    if ss == 60:
        mm += 1
        ss = 0
    if mm == 60:
        hh += 1
        mm = 0
    if hh == 24:
        hh = 0

    busy_robots = 0
    for robot in robots_info:
        if robots_info[robot]["availability"]:
            print(f"{robot} - {products.popleft()} [{hh:02d}:{mm:02d}:{ss:02d}]")
            robots_info[robot]["availability"] = False
            break
        busy_robots += 1
    if busy_robots == len(robots_info):
        products.rotate(-1)

    for robot in robots_info:
        if not robots_info[robot]["availability"] and not robots_info[robot]["process_time"] == 0:
            robots_info[robot]["time_until_available"] -= 1
            if robots_info[robot]["time_until_available"] == 0:
                robots_info[robot]["availability"] = True
                robots_info[robot]["time_until_available"] = robots_info[robot]["process_time"]
        else:
            robots_info[robot]["availability"] = True
