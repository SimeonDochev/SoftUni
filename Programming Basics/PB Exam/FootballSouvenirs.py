team = input()
souvenir = input()
amount = int(input())

total_price = 0
flag = False

if team == 'Argentina':
    if souvenir == 'flags':
        total_price += amount * 3.25
    elif souvenir == 'caps':
        total_price += amount * 7.2
    elif souvenir == 'posters':
        total_price += amount * 5.1
    elif souvenir == 'stickers':
        total_price += amount * 1.25
    else:
        print('Invalid stock!')
        flag = True
elif team == 'Brazil':
    if souvenir == 'flags':
        total_price += amount * 4.2
    elif souvenir == 'caps':
        total_price += amount * 8.5
    elif souvenir == 'posters':
        total_price += amount * 5.35
    elif souvenir == 'stickers':
        total_price += amount * 1.20
    else:
        print('Invalid stock!')
        flag = True
elif team == 'Croatia':
    if souvenir == 'flags':
        total_price += amount * 2.75
    elif souvenir == 'caps':
        total_price += amount * 6.9
    elif souvenir == 'posters':
        total_price += amount * 4.95
    elif souvenir == 'stickers':
        total_price += amount * 1.10
    else:
        print('Invalid stock!')
        flag = True
elif team == 'Denmark':
    if souvenir == 'flags':
        total_price += amount * 3.10
    elif souvenir == 'caps':
        total_price += amount * 6.5
    elif souvenir == 'posters':
        total_price += amount * 4.8
    elif souvenir == 'stickers':
        total_price += amount * 0.9
    else:
        print('Invalid stock!')
        flag = True
else:
    print('Invalid country!')
    flag = True

if not flag:
    print(f'Pepi bought {amount} {souvenir} of {team} for {total_price:.2f} lv.')