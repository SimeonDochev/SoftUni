n = int(input())

reservations = set()

for _ in range(n):
    reservations.add(input())

reservation_code = input()
while not reservation_code == "END":
    reservations.discard(reservation_code)
    reservation_code = input()

print(len(reservations))
for code in sorted(reservations):
    print(code)
