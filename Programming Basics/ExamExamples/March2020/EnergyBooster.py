fruit = input()
size = input()
quantity = int(input())

total_price = 0

if size == 'small':
    if fruit == 'Watermelon':
        total_price = quantity * (56 * 2)
    elif fruit == 'Mango':
        total_price = quantity * (36.66 * 2)
    elif fruit == 'Pineapple':
        total_price = quantity * (42.10 * 2)
    elif fruit == 'Raspberry':
        total_price = quantity * (20 * 2)
    if 400 <= total_price <= 1000:
        total_price = total_price * 0.85
    elif total_price > 1000:
        total_price = total_price * 0.5
elif size == 'big':
    if fruit == 'Watermelon':
        total_price = quantity * (28.7 * 5)
    elif fruit == 'Mango':
        total_price = quantity * (19.6 * 5)
    elif fruit == 'Pineapple':
        total_price = quantity * (24.8 * 5)
    elif fruit == 'Raspberry':
        total_price = quantity * (15.2 * 5)
    if 400 <= total_price <= 1000:
        total_price = total_price * 0.85
    elif total_price > 1000:
        total_price = total_price * 0.5

print(f'{total_price:.2f} lv.')