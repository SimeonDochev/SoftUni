minutes_walk = int(input())
walks_per_day = int(input())
daily_calories = int(input())

calories_burnt = minutes_walk * walks_per_day * 5

if calories_burnt >= daily_calories / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.')
