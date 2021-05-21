employees_efficiency = 0

for _ in range(3):
    efficiency = int(input())
    employees_efficiency += efficiency

students_count = int(input())
hours = 0

while students_count > 0:
    students_count -= employees_efficiency
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
