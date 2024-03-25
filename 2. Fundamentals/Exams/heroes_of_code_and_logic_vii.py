def cast_spell(hero_party, split_command):
    hero_name = split_command[1]
    mana_needed = int(split_command[2])
    spell_name = split_command[3]
    if hero_party[hero_name]["MP"] >= mana_needed:
        hero_party[hero_name]["MP"] -= mana_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {hero_party[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return hero_party


def take_damage(hero_party, split_command):
    hero_name = split_command[1]
    damage = int(split_command[2])
    attacker_name = split_command[3]
    hero_party[hero_name]["HP"] -= damage
    if hero_party[hero_name]["HP"] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker_name} and now has "
              f"{hero_party[hero_name]['HP']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker_name}!")
        del hero_party[hero_name]
    return hero_party


def recharge(hero_party, split_command):
    hero_name = split_command[1]
    recharge_amount = int(split_command[2])
    if hero_party[hero_name]["MP"] + recharge_amount <= 200:
        hero_party[hero_name]["MP"] += recharge_amount
        recharged_mana = recharge_amount
    else:
        recharged_mana = 200 - hero_party[hero_name]["MP"]
        hero_party[hero_name]["MP"] = 200
    print(f"{hero_name} recharged for {recharged_mana} MP!")
    return hero_party


def heal(hero_party, split_command):
    hero_name = split_command[1]
    heal_amount = int(split_command[2])
    if hero_party[hero_name]["HP"] + heal_amount <= 100:
        healed_health = heal_amount
        hero_party[hero_name]["HP"] += heal_amount
    else:
        healed_health = 100 - hero_party[hero_name]["HP"]
        hero_party[hero_name]["HP"] = 100
    print(f"{hero_name} healed for {healed_health} HP!")
    return hero_party


number_of_heroes = int(input())

party = {}

for hero in range(number_of_heroes):
    current_hero = input().split()
    current_hero_name = current_hero[0]
    hero_hp = int(current_hero[1])
    hero_mp = int(current_hero[2])
    if current_hero_name not in party:
        party[current_hero_name] = {"HP": hero_hp, "MP": hero_mp}

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        cast_spell(party, command)

    elif action == "TakeDamage":
        take_damage(party, command)

    elif action == "Recharge":
        recharge(party, command)

    elif action == "Heal":
        heal(party, command)

for member, stats in party.items():
    print(member)
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")
