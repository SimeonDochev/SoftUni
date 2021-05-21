courses_data = {}

command = input()
while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_data:
        courses_data[course_name] = [student_name]
    else:
        courses_data[course_name].append(student_name)
    command = input()

for course in sorted(courses_data, key=lambda k: len(courses_data[k]), reverse=True):
    print(f"{course}: {len(courses_data[course])}")
    for student in sorted(courses_data[course]):
        print(f"-- {student}")
