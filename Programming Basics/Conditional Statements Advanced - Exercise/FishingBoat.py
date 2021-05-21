budget = int(input())
season = input()
count = int(input())
rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if count <= 6:
    rent *= 0.9
elif 7 <= count <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if count % 2 == 0 and season != 'Autumn':
    rent *= 0.95
else:
    rent *= 1

if rent <= budget:
    print(f'Yes! You have {budget - rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {rent - budget:.2f} leva.')
