flowers = input()
quantity = int(input())
budget = int(input())
price = 0

if flowers == 'Roses':
    if quantity > 80:
        price = (quantity * 5) * 0.9
    else:
        price = quantity * 5
elif flowers == 'Dahlias':
    if quantity > 90:
        price = (quantity * 3.8) * 0.85
    else:
        price = quantity * 3.8
elif flowers == 'Tulips':
    if quantity > 80:
        price = (quantity * 2.8) * 0.85
    else:
        price = quantity * 2.8
elif flowers == 'Narcissus':
    if quantity < 120:
        price = (quantity * 3) * 1.15
    else:
        price = quantity * 3
elif flowers == 'Gladiolus':
    if quantity < 80:
        price = (quantity * 2.5) * 1.2
    else:
        price = quantity * 2.5

if price <= budget:
    print(f'Hey, you have a great garden with {quantity} {flowers} and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')