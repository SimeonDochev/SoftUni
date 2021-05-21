budget = float(input())
season = input()

if budget <= 100:
    if season == 'summer':
        print(f'Somewhere in Bulgaria')
        print(f'Camp - {budget * 0.3:.2f}')
    elif season == 'winter':
        print(f'Somewhere in Bulgaria')
        print(f'Hotel - {budget * 0.7:.2f}')
elif 100 < budget <= 1000:
    if season == 'summer':
        print(f'Somewhere in Balkans')
        print(f'Camp - {budget * 0.4:.2f}')
    elif season == 'winter':
        print(f'Somewhere in Balkans')
        print(f'Hotel - {budget * 0.8:.2f}')
else:
    print(f'Somewhere in Europe')
    print(f'Hotel - {budget * 0.9:.2f}')

