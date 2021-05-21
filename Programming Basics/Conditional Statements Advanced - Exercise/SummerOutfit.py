degrees = int(input())
time_of_day = input()

if time_of_day == 'Morning':
    if 10 <= degrees <= 18:
        print(f'It\'s {degrees} degrees, get your Sweatshirt and Sneakers.')
    elif 18 < degrees <= 24:
        print(f'It\'s {degrees} degrees, get your Shirt and Moccasins.')
    else:
        print(f'It\'s {degrees} degrees, get your T-Shirt and Sandals.')
if time_of_day == 'Afternoon':
    if 10 <= degrees <= 18:
        print(f'It\'s {degrees} degrees, get your Shirt and Moccasins.')
    elif 18 < degrees <= 24:
        print(f'It\'s {degrees} degrees, get your T-Shirt and Sandals.')
    else:
        print(f'It\'s {degrees} degrees, get your Swim Suit and Barefoot.')
if time_of_day == 'Evening':
    if 10 <= degrees <= 18:
        print(f'It\'s {degrees} degrees, get your Shirt and Moccasins.')
    elif 18 < degrees <= 24:
        print(f'It\'s {degrees} degrees, get your Shirt and Moccasins.')
    else:
        print(f'It\'s {degrees} degrees, get your Shirt and Moccasins.')
