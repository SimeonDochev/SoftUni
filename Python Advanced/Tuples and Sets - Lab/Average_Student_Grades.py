n = int(input())

students_data = {}

for _ in range(n):
    student, grade = input().split()
    if student not in students_data:
        students_data[student] = []
    students_data[student].append(float(grade))

for student in students_data:
    current_student_grades = ' '.join(map(lambda grade: f'{grade:.2f}', students_data[student]))
    avg_grade = sum(students_data[student])/len(students_data[student])
    print(f"{student} -> {current_student_grades} (avg: {avg_grade:.2f})")
