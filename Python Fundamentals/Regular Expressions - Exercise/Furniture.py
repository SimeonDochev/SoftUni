import re

text = input()
pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(.\d+)?)!(?P<quantity>\d+)"
furniture_items = []
total_price = 0

while not text == "Purchase":
    match = re.match(pattern, text)
    if match:
        match.groupdict()
        furniture_items.append(match["name"])
        total_price += float(match["price"]) * int(match["quantity"])
    text = input()

print("Bought furniture:")
for item in furniture_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")
