employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())

employees_happiness = list(map(lambda x: x * happiness_improvement_factor, employees_happiness))

filtered_happy_employees = list(filter(lambda x: x >= sum(employees_happiness) / len(employees_happiness), employees_happiness))

if len(filtered_happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered_happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
