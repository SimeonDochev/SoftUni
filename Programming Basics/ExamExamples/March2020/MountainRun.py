record_in_seconds = float(input())
distance = float(input())
time_for_one_meter = float(input())

slow = distance // 50 * 30
total_time = distance * time_for_one_meter + slow

if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record_in_seconds:.2f} seconds slower.')