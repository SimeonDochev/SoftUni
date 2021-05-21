bitcoin_quantity = int(input())
yuan_quantity = float(input())
commission = float(input())

bitcoin_price_euro = 1168 / 1.95
yuan_price_euro = 0.15 * 1.76 / 1.95
total_sum = bitcoin_price_euro * bitcoin_quantity + yuan_price_euro * yuan_quantity
result = total_sum - total_sum * commission / 100

print(f'{result:.2f}')