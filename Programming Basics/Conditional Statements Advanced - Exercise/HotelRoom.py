month = input()
nights = int(input())
price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    if 7 < nights < 14:
        price_studio = (nights * 50) * 0.95
        price_apartment = nights * 65
    elif nights > 14:
        price_studio = (nights * 50) * 0.7
        price_apartment = (nights * 65) * 0.9
    else:
        price_studio = nights * 50
        price_apartment = nights * 65
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
elif month == 'June' or month == 'September':
    if nights > 14:
        price_studio = (nights * 75.2) * 0.8
        price_apartment = (nights * 68.7) * 0.9
    else:
        price_studio = nights * 75.2
        price_apartment = nights * 68.7
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
elif month == 'July' or month == 'August':
    if nights > 14:
        price_studio = nights * 76
        price_apartment = (nights * 77) * 0.9
    else:
        price_studio = nights * 76
        price_apartment = nights * 77
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')