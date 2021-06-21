from collections import deque

orders = deque(int(el) for el in input().split(', '))
employees_capacity = [int(el) for el in input().split(', ')]

total_pizzas = 0
current_order = None

while orders:
    if not current_order:
        current_order = orders.popleft()
    if current_order <= 0 or current_order > 10:
        current_order = None
        continue
    current_employee_capacity = employees_capacity.pop()
    if current_order <= current_employee_capacity:
        total_pizzas += current_order
        current_order = None
        continue
    elif current_order > current_employee_capacity:
        current_order -= current_employee_capacity
        total_pizzas += current_employee_capacity
        if employees_capacity:
            continue
        else:
            orders.appendleft(current_order)
            break

if not orders and employees_capacity:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(el) for el in employees_capacity])}")
elif orders and not employees_capacity:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in orders])}")
