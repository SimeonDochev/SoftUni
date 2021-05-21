from collections import deque

total_food = int(input())
orders_queue = deque(list(map(int, input().split())))

print(max(orders_queue))

while orders_queue:
    if total_food >= orders_queue[0]:
        total_food -= orders_queue.popleft()
    else:
        break

orders_queue = list(map(str, orders_queue))

if not orders_queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(orders_queue)}")
