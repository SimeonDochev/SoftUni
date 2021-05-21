days = int(input())
food_quantity = float(input())

dog_sum = 0
cat_sum = 0
biscuits = 0

for i in range(1, days + 1):
    daily = 0
    dog = int(input())
    dog_sum += dog
    daily += dog
    cat = int(input())
    cat_sum += cat
    daily += cat
    if i % 3 == 0:
        biscuits += daily * 0.1

total = dog_sum + cat_sum

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total / food_quantity * 100:.2f}% of the food has been eaten.')
print(f'{dog_sum / total * 100:.2f}% eaten from the dog.')
print(f'{cat_sum / total * 100:.2f}% eaten from the cat.')
