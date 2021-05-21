duration = int(input())

total_money = 0
total_wins = 0
total_losses = 0

for i in range(duration):
    daily_wins = 0
    daily_losses = 0
    daily_money = 0
    command = input()
    while command != 'Finish':
        outcome = input()
        if outcome == 'win':
            daily_money += 20
            daily_wins += 1
            total_wins += 1
        else:
            daily_losses += 1
            total_losses += 1
        command = input()
    if daily_wins > daily_losses:
        daily_money *= 1.1
    total_money += daily_money

if total_wins > total_losses:
    print(f'You won the tournament! Total raised money: {total_money * 1.2:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')