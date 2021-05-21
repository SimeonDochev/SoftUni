hour = int(input())
day = input()

if hour < 10 or hour > 18 or day == 'Sunday':
    print('closed')
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday':
    if hour < 10 or hour > 18:
        print('closed')
    else:
        print('open')