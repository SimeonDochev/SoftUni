products_list = input().split()

products_dict = {}

for i in range(0, len(products_list), 2):
    product, quantity = products_list[i], products_list[i + 1]
    quantity = int(quantity)
    products_dict[product] = quantity

print(products_dict)
