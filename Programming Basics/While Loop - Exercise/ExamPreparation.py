fails_allowed = int(input())
fails = 0
grades_sum = 0
count = 0
last_problem = ''

while fails < fails_allowed:
    problem = input()
    if problem == 'Enough':
        print(f'Average score: {grades_sum/count:.2f}')
        print(f'Number of problems: {count}')
        print(f'Last problem: {last_problem}')
        break
    grade = int(input())
    if grade <= 4:
        fails += 1
    grades_sum += grade
    count += 1
    last_problem = problem

if fails >= fails_allowed:
    print(f'You need a break, {fails} poor grades.')
