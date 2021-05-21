def cast_spell(account, hero_name, mana_needed, spell_name):
    if account[hero]['mana'] >= mana_needed:
        account[hero_name]['mana'] -= mana_needed
        return f"{hero_name} has successfully cast {spell_name} and now has {account[hero_name]['mana']} MP!"
    return f"{hero} does not have enough MP to cast {spell_name}!"


def take_damage(account, hero_name, damage, attacker):
    if account[hero_name]['HP'] - damage > 0:
        account[hero_name]['HP'] -= damage
        return f"{hero_name} was hit for {damage} HP by {attacker} and now has {account[hero_name]['HP']} HP left!"
    account.pop(hero_name)
    return f"{hero_name} has been killed by {attacker}!"


def recharge(account, hero_name, amount):
    if account[hero_name]['mana'] + amount <= 200:
        account[hero_name]['mana'] += amount
        return f"{hero_name} recharged for {amount} MP!"
    recharged_amount = 200 - account[hero_name]['mana']
    account[hero_name]['mana'] = 200
    return f"{hero_name} recharged for {recharged_amount} MP!"


def heal(account, hero_name, amount):
    if account[hero_name]['HP'] + amount <= 100:
        account[hero_name]['HP'] += amount
        return f"{hero_name} healed for {amount} HP!"
    healed_amount = 100 - account[hero_name]['HP']
    account[hero_name]['HP'] = 100
    return f"{hero_name} healed for {healed_amount} HP!"


n = int(input())

account = {}

for _ in range(n):
    hero_name, hp, mana = input().split()
    hp = int(hp)
    mana = int(mana)
    account[hero_name] = {'HP': hp, 'mana': mana}

command = input()
while not command == "End":
    command_data = command.split(" - ")
    action = command_data[0]
    hero = command_data[1]
    if action == "CastSpell":
        mana_needed = int(command_data[2])
        spell_name = command_data[3]
        print(cast_spell(account, hero, mana_needed, spell_name))
    elif action == "TakeDamage":
        damage = int(command_data[2])
        attacker = command_data[3]
        print(take_damage(account, hero, damage, attacker))
    elif action == "Recharge":
        amount = int(command_data[2])
        print(recharge(account, hero, amount))
    elif action == "Heal":
        amount = int(command_data[2])
        print(heal(account, hero, amount))
    command = input()

for hero, info in sorted(account.items(), key=lambda kvp: (-kvp[1]['HP'], kvp[0])):
    print(hero)
    print(f"  HP: {info['HP']}")
    print(f"  MP: {info['mana']}")
