customers_count = int(input())

bills_sum = 0

for i in range(customers_count):
    bill = 0
    products_count = 0
    command = input()
    while command != 'Finish':
        products_count += 1
        if command == 'basket':
            bill += 1.5
        elif command == 'wreath':
            bill += 3.8
        elif command == 'chocolate bunny':
            bill += 7
        command = input()
    if products_count % 2 == 0:
        bill *= 0.8
    bills_sum += bill
    print(f'You purchased {products_count} items for {bill:.2f} leva.')

print(f'Average bill per client is: {bills_sum / customers_count:.2f} leva.')

