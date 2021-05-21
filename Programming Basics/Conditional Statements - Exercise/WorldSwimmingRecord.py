from math import floor

record = float(input())
distance = float(input())
time_for_one_meter = float(input())
added_time = (distance // 15) * 12.5
total_time = time_for_one_meter * distance + added_time

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(total_time - record):.2f} seconds slower.')
