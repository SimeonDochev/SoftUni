exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_time = exam_hours * 60 + exam_minutes
arrival_time = arrival_hours * 60 + arrival_minutes
diff = arrival_time - exam_time

if arrival_time == exam_time:
    print('On time')
elif arrival_time > exam_time:
    print('Late')
    if diff >= 60:
        print(f'{abs(diff) // 60}:{abs(diff) % 60:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif arrival_time < exam_time:
    if abs(diff) <= 30:
        print('On time')
        print(f'{abs(diff)} minutes before the start')
    elif abs(diff) >= 60:
        print('Early')
        print(f'{abs(diff) // 60}:{abs(diff) % 60:02d} hours before the start')
    else:
        print('Early')
        print(f'{abs(diff)} minutes before the start')
