excursion_price = float(input())
puzzle_amount = int(input())
dolls_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())
puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2
toys_count = puzzle_amount + dolls_amount + bears_amount + minions_amount + trucks_amount
toys_price = puzzle_price * puzzle_amount + doll_price * dolls_amount + bear_price * bears_amount + minion_price * minions_amount + truck_price * trucks_amount

if toys_count >= 50:
    toys_price = toys_price * 0.75
else:
    toys_price = toys_price

rent = toys_price * 0.1
total_income = toys_price - rent
amount_left = total_income - excursion_price
money_needed = abs(excursion_price - total_income)

if total_income >= excursion_price:
    print(f'Yes! {amount_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_needed:.2f} lv needed. ')
