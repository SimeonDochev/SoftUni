products = {}

command = input()
while not command == "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
