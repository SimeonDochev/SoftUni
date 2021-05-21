party_size = int(input())
days = int(input())

profit = 0

for day in range(1, days+1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    profit += 50 - 2 * party_size
    if day % 3 == 0:
        profit -= 3 * party_size
    if day % 5 == 0:
        profit += 20 * party_size
        if day % 3 == 0:
            profit -= 2 * party_size

print(f"{party_size} companions received {int(profit / party_size)} coins each.")