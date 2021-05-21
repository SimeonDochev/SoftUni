pens_quantity = int(input())
markers_quantity = int(input())
liters = float(input())
discount_percentage = int(input())

pens_price = 5.8
markers_price = 7.2
liter_price = 1.2

total_sum = pens_quantity * pens_price + markers_quantity * markers_price + liters * liter_price
result = total_sum - total_sum * discount_percentage / 100

print(f'{result:.3f}')
