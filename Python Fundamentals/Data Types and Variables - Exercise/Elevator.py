from math import ceil

number_of_people = int(input())
capacity_of_elevator = int(input())

course_count = number_of_people / capacity_of_elevator

print(ceil(course_count))