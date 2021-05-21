import re

text = input()
pattern = r"(?P<separator>#|\|)(?P<product_name>[a-zA-Z\s]+)(?P=separator)(?P<expiration_date>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)"
total_calories = 0

products_data = [obj.groupdict() for obj in re.finditer(pattern, text)]

for data in products_data:
    total_calories += int(data["calories"])

print(f"You have food to last you for: {total_calories//2000} days!")
for product in products_data:
    print('\n'.join([f"Item: {product['product_name']}, Best before: {product['expiration_date']}, Nutrition: {product['calories']}"]))
