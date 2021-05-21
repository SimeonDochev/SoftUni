products_list = input().split()

products_dict = {}

for i in range(0, len(products_list), 2):
    product, quantity = products_list[i], products_list[i+1]
    quantity = int(quantity)
    products_dict[product] = quantity

products_requests = input().split()

for prod in products_requests:
    if prod in products_dict:
        print(f"We have {products_dict[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")
