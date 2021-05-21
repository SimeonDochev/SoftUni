fire_cells_list = input().split("#")
water = int(input())

total_effort = 0
total_fire = 0

fire_cells_order = []

for fire in range(len(fire_cells_list)):
    current_fire_info_list = fire_cells_list[fire].split()
    current_fire_type = current_fire_info_list[0]
    current_fire_size = int(current_fire_info_list[2])
    if water < current_fire_size:
        continue
    if current_fire_type == "High" and 81 <= current_fire_size <= 125:
        water -= current_fire_size
        total_fire += current_fire_size
        total_effort += current_fire_size * 0.25
        fire_cells_order.append(current_fire_size)
    elif current_fire_type == "Medium" and 51 <= current_fire_size <= 80:
        water -= current_fire_size
        total_fire += current_fire_size
        total_effort += current_fire_size * 0.25
        fire_cells_order.append(current_fire_size)
    elif current_fire_type == "Low" and 1 <= current_fire_size <= 50:
        water -= current_fire_size
        total_fire += current_fire_size
        total_effort += current_fire_size * 0.25
        fire_cells_order.append(current_fire_size)

print("Cells:")
for i in range(len(fire_cells_order)):
    print(f" - {fire_cells_order[i]}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire:}")
