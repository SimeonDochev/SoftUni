cats_count = int(input())

group1 = 0
group2 = 0
group3 = 0
total_food = 0
for i in range(cats_count):
    food_grams = float(input())
    if 100 <= food_grams < 200:
        total_food += food_grams
        group1 += 1
    elif 200 <= food_grams < 300:
        total_food += food_grams
        group2 += 1
    elif 300 <= food_grams < 400:
        total_food += food_grams
        group3 += 1

print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {total_food / 1000 * 12.45:.2f} lv.')
