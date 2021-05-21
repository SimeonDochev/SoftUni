capacity = 255
lines_num = int(input())
quantity_filled = 0

for i in range(lines_num):
    water_quantity = int(input())
    capacity -= water_quantity
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += water_quantity
    else:
        quantity_filled += water_quantity

print(quantity_filled)