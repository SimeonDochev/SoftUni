import re

text = input()
pattern = r"(?P<separator>=|/)(?P<destination>[A-Z][a-zA-Z]{2,})(?P=separator)"
travel_points = 0

valid_destinations = []
for obj in re.finditer(pattern, text):
    valid_destinations.append(obj.group('destination'))

for destination in valid_destinations:
    travel_points += len(destination)

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")
