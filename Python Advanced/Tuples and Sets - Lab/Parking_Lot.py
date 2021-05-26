n = int(input())

parking = set()

for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        parking.add(plate)
    else:
        parking.discard(plate)

if not parking:
    print("Parking Lot is Empty")
else:
    print('\n'.join(parking))