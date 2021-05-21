days = int(input())
room = input()
review = input()
room_price = 18
apartment_price = 25
president_price = 35
total_price = 0

if room == 'room for one person':
    total_price = room_price * (days - 1)
elif room == 'apartment':
    if days < 10:
        total_price = (apartment_price * (days - 1)) * 0.7
    elif 10 <= days <= 15:
        total_price = (apartment_price * (days - 1)) * 0.65
    elif days > 15:
        total_price = (apartment_price * (days - 1)) * 0.5
elif room == 'president apartment':
    if days < 10:
        total_price = (president_price * (days - 1)) * 0.9
    elif 10 <= days <= 15:
        total_price = (president_price * (days - 1)) * 0.85
    elif days > 15:
        total_price = (president_price * (days - 1)) * 0.8

if review == 'positive':
    total_price += total_price * 0.25
elif review == 'negative':
    total_price -= total_price * 0.1

print(f'{total_price:.2f}')
