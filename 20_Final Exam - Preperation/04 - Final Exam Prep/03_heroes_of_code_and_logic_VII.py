number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    current_hero, health, mana = input().split()
    if current_hero not in heroes:
        heroes[current_hero] = {"HP": 0, "MP": 0}
    heroes[current_hero]["HP"] += int(health)
    heroes[current_hero]["MP"] += int(mana)

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    action = command[0]
    if action == "CastSpell":
        hero, needed_mana, spell_name = command[1], int(command[2]), command[3]
        if heroes[hero]["MP"] >= needed_mana:
            heroes[hero]["MP"] -= needed_mana
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero, damage, attacker = command[1], int(command[2]), command[3]
        heroes[hero]["HP"] -= damage
        if heroes[hero]["HP"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            heroes.pop(hero)
    elif action == "Recharge":
        hero, amount_mana = command[1], int(command[2])
        maximum_mana = 200
        mana_to_add = min(amount_mana, maximum_mana - heroes[hero]['MP'])
        heroes[hero]['MP'] += mana_to_add
        print(f"{hero} recharged for {mana_to_add} MP!")
    elif action == "Heal":
        hero, amount_health = command[1], int(command[2])
        maximum_health = 100
        health_to_add = min(amount_health, maximum_health - heroes[hero]['HP'])
        heroes[hero]['HP'] += health_to_add
        print(f'{hero} healed for {health_to_add} HP!')

for hero, hp_mp in heroes.items():
    print(f"{hero}")
    print(f"HP: {hp_mp['HP']}")
    print(f"MP: {hp_mp['MP']}")