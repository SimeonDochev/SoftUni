destination = input()

current_budget = 0

while destination != 'End':
    budget_needed = float(input())
    while current_budget < budget_needed:
        money = float(input())
        current_budget += money
    else:
        print(f'Going to {destination}!')
        current_budget = 0
    destination = input()

