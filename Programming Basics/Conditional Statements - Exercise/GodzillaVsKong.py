budget = float(input())
statists = int(input())
outfit_price = float(input())
total_outfit_price = outfit_price * statists
decor_price = budget * 0.1

if statists > 150:
    total_outfit_price = total_outfit_price * 0.9

if decor_price + total_outfit_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {abs(budget - (total_outfit_price + decor_price)):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - (total_outfit_price + decor_price):.2f} leva left.')
