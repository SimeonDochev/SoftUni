countries = input().split(', ')
capitals = input().split(', ')

combinations = dict(zip(countries, capitals))

for country, capital in combinations.items():
    print(f"{country} -> {capital}")
