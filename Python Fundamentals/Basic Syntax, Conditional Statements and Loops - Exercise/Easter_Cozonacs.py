budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
cozonac_price = eggs_price + flour_price + milk_price

cozonacs_count = 0
colored_eggs_count = 0

while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs_count += 3
    if cozonacs_count % 3 == 0:
        colored_eggs_count -= (cozonacs_count - 2)

print(f'You made {cozonacs_count} cozonacs! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')