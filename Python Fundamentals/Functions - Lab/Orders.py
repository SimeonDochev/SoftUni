def calculate_total_price(prod, quan):
    if prod == "coffee":
        return quan * COFFEE_PRICE
    elif prod == "water":
        return quan * WATER_PRICE
    elif prod == "coke":
        return quan * COKE_PRICE
    elif prod == "snacks":
        return quan * SNACKS_PRICE


COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00

product = input()
quantity = int(input())

print(f"{calculate_total_price(product, quantity):.2f}")