from math import floor

year_type = input()
p = int(input())
h = int(input())
weekends_in_sofia = 48 - h
games_in_sofia = weekends_in_sofia * (3 / 4)
games_on_holidays = (p * (2 / 3))
total_games = 0

if year_type == 'normal':
    total_games = games_in_sofia + h + games_on_holidays
elif year_type == 'leap':
    total_games = (games_in_sofia + h + games_on_holidays) * 1.15
print(f'{floor(total_games)}')
