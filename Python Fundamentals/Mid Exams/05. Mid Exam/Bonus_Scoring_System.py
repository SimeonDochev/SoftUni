students_count = int(input())
lectures_count = int(input())
course_bonus = int(input())

max_bonus = 0
max_attendance = 0

for student in range(students_count):
    student_attendances = int(input())
    current_student_bonus = student_attendances / lectures_count * (5 + course_bonus)
    if current_student_bonus > max_bonus:
        max_bonus = current_student_bonus
        max_attendance = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
