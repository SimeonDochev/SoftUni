experience_needed = float(input())
battles_count = int(input())

is_won = False

battle = 1
current_experience = 0

for i in range(battles_count):
    experience = float(input())
    if battle % 15 == 0:
        current_experience += experience * 1.05
    elif battle % 5 == 0:
        current_experience += experience * 0.9
    elif battle % 3 == 0:
        current_experience += experience * 1.15
    else:
        current_experience += experience
    if current_experience >= experience_needed:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        is_won = True
        break
    battle += 1

if not is_won:
    exp_lack = experience_needed - current_experience
    print(f"Player was not able to collect the needed experience, {exp_lack:.2f} more needed.")
