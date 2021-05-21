strawberry_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

total = (strawberries_quantity * strawberry_price + bananas_quantity * bananas_price + oranges_quantity * oranges_price + raspberries_quantity * raspberries_price)

print(total)