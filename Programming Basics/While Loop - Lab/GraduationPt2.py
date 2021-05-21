name = input()
year = 0
fails = 0
grades_sum = 0

while year < 12:
    grade = float(input())
    if grade >= 4:
        grades_sum += grade
        year += 1
    else:
        fails += 1
    if fails == 2:
        print(f'{name} has been excluded at {year+1} grade')
        break

if year == 12:
    print(f'{name} graduated. Average grade: {grades_sum / 12:.2f}')