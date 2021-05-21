clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())

racks_used = 0

while clothes_stack:
    current_rack = 0
    while current_rack + clothes_stack[-1] <= rack_capacity:
        current_rack += clothes_stack.pop()
        if not clothes_stack:
            break
    racks_used += 1
print(racks_used)