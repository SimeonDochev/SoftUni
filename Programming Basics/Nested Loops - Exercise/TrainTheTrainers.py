judges = int(input())
total_grades_sum = 0
total_counter = 0

command = input()
while command != 'Finish':
    counter = 0
    grades_sum = 0
    for i in range(judges):
        grade = float(input())
        counter += 1
        total_counter += 1
        grades_sum += grade
        total_grades_sum += grade
    print(f'{command} - {grades_sum / judges:.2f}.')
    command = input()

print(f'Student\'s final assessment is {total_grades_sum / total_counter:.2f}.')
