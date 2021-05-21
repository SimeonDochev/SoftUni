total_price = 0

command = input()
while not command == "special" and not command == "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price += price
    command = input()

if total_price > 0:
    taxes = total_price * 0.2
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    if command == "special":
        price_with_discount = (total_price + taxes) * 0.9
        print(f"Total price: {price_with_discount:.2f}$")
    else:
        print(f"Total price: {total_price + taxes:.2f}$")
else:
    print("Invalid order!")
