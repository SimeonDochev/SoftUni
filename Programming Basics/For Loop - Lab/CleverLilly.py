age = int(input())
laundry_price = float(input())
toy_price = int(input())

savings = 0

for i in range(1, age+1):
    if i % 2 == 0:
        savings += (i * 10 / 2) - 1
    else:
        savings += toy_price


if savings >= laundry_price:
    print(f'Yes! {savings - laundry_price:.2f}')
else:
    print(f'No! {laundry_price - savings:.2f}')
