from collections import deque

names = deque(input().split())
count = int(input())

while len(names) > 1:
    names.rotate(-count)
    print(f"Removed {names.pop()}")

print(f"Last is {names.pop()}")
