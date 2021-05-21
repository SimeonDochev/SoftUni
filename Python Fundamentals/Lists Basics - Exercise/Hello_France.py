items_list = input().split("|")
budget = float(input())

new_prices = []
profit = 0

for item in range(len(items_list)):
    current_item_details = items_list[item].split("->")
    current_item_type = current_item_details[0]
    current_item_price = float(current_item_details[1])
    if current_item_type == "Clothes":
        if current_item_price > 50:
            continue
        if current_item_price <= budget:
            budget -= current_item_price
            new_prices.append(current_item_price * 1.4)
            profit += current_item_price * 1.4 - current_item_price
    elif current_item_type == "Shoes":
        if current_item_price > 35:
            continue
        if current_item_price <= budget:
            budget -= current_item_price
            new_prices.append(current_item_price * 1.4)
            profit += current_item_price * 1.4 - current_item_price
    elif current_item_type == "Accessories":
        if current_item_price > 20.50:
            continue
        if current_item_price <= budget:
            budget -= current_item_price
            new_prices.append(current_item_price * 1.4)
            profit += current_item_price * 1.4 - current_item_price

for price in range(len(new_prices)):
    print(f"{new_prices[price]:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(new_prices) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
