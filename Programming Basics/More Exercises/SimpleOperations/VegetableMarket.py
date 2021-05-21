price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total_price_vegetables = price_kg_vegetables * total_kg_vegetables
total_price_fruits = price_kg_fruits * total_kg_fruits
total_income = (total_price_fruits + total_price_vegetables) / 1.94

print(f'{total_income:.2f}')

