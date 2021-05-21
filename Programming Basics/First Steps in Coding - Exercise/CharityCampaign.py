days_count = int(input())
cooks_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_total = cakes_count * 45
waffles_total = waffles_count * 5.8
pancakes_total = pancakes_count * 3.2

daily_money = (cakes_total + waffles_total + pancakes_total) * cooks_count
total_money = daily_money * days_count
total_money -= total_money / 8
print(total_money)

