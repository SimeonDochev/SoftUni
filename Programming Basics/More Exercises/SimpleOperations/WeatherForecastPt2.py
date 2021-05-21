temperature = float(input())

if 5 <= temperature < 12:
    print('Cold')
elif 12 <= temperature < 15:
    print('Cool')
elif 15 <= temperature <= 20:
    print('Mild')
elif 20 < temperature < 26:
    print('Warm')
elif 26 <= temperature <= 35:
    print(f'Hot')
else:
    print('unknown')
