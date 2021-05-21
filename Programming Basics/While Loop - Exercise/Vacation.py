money_needed = float(input())
money = float(input())
days_count = 0
spending_count = 0

while money < money_needed and spending_count < 5:
    command = input()
    amount = float(input())
    days_count += 1
    if command == 'save':
        money += amount
        spending_count = 0
    elif command == 'spend':
        money -= amount
        spending_count += 1
        if money < 0:
            money = 0
if spending_count == 5:
    print(f'You can\'t save the money.')
    print(f'{days_count}')
if money >= money_needed:
    print(f'You saved the money for {days_count} days.')