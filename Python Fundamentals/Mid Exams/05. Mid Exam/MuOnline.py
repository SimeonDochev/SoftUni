health = 100
bitcoins = 0

is_dead = False
best_room = 1

list_of_actions = input().split("|")

for action_data in list_of_actions:
    action, amount = action_data.split()
    amount = int(amount)
    if action == "potion":
        if health + amount > 100:
            healed_amount = 100 - health
            health = 100
            print(f"You healed for {healed_amount} hp.")
        else:
            health += amount
            print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        if health - amount > 0:
            health -= amount
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            is_dead = True
            break
    best_room += 1

if not is_dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
