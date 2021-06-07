from collections import deque

cups = deque(int(el) for el in input().split())
bottles = [int(el) for el in input().split()]

wasted_litters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    difference = current_bottle - current_cup
    if difference < 0:
        cups.appendleft(current_cup - current_bottle)
    elif difference > 0:
        wasted_litters += difference

if bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}")
    print(f"Wasted litters of water: {wasted_litters}")
if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
    print(f"Wasted litters of water: {wasted_litters}")
