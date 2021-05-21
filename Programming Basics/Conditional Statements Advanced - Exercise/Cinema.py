projection_type = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns

if projection_type == 'Premiere':
    income = capacity * 12
elif projection_type == 'Normal':
    income = capacity * 7.5
elif projection_type == 'Discount':
    income = capacity * 5

print(f'{income:.2f} leva')
