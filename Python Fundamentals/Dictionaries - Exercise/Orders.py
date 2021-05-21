products_data = {}

command = input()
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_data:
        products_data[name] = [price, quantity]
    else:
        products_data[name][0] = price
        products_data[name][1] += quantity
    command = input()

for name, data in products_data.items():
    print(f"{name} -> {(data[0] * data[1]):.2f}")
