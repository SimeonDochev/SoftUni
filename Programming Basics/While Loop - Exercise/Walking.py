steps_count = 0

while steps_count < 10000:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_count += steps
        break
    steps = int(steps)
    steps_count += steps

if steps_count >= 10000:
    print('Goal reached! Good job!')
    print(f'{steps_count - 10000} steps over the goal!')
else:
    print(f'{10000-steps_count} more steps to reach goal.')