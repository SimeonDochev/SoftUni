database = {}

n = int(input())

for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in database:
        database[student_name] = [grade]
    else:
        database[student_name].append(grade)

filtered_database = {}

for student, grades in database.items():
    average_grade = sum(grades)/len(grades)
    if average_grade >= 4.5:
        filtered_database[student] = average_grade

for student, avg_grade in sorted(filtered_database.items(), key=lambda k: -k[1]):
    print(f"{student} -> {avg_grade:.2f}")
