def plunder(cities_dict, split_command):
    plundered_city = split_command[1]
    killed_citizens = int(split_command[2])
    stolen_gold = int(split_command[3])
    cities_dict[plundered_city]["Population"] -= killed_citizens
    cities_dict[plundered_city]["Gold"] -= stolen_gold
    print(f"{plundered_city} plundered! {stolen_gold} gold stolen, {killed_citizens} citizens killed.")
    if cities_dict[plundered_city]["Population"] <= 0 or cities_dict[plundered_city]["Gold"] <= 0:
        print(f"{plundered_city} has been wiped off the map!")
        del cities_dict[plundered_city]
    return cities_dict


def prosper(cities_dict, split_command):
    prospered_city = split_command[1]
    prospered_gold = int(split_command[2])
    if prospered_gold <= 0:
        print("Gold added cannot be a negative number!")
        return cities_dict
    cities_dict[prospered_city]["Gold"] += prospered_gold
    print(f"{prospered_gold} gold added to the city treasury. {prospered_city} now has "
          f"{cities_dict[prospered_city]['Gold']} gold.")


cities = {}

while True:
    command = input()

    if command == "Sail":
        break

    city_name, population, gold = command.split("||")

    if city_name not in cities:
        cities[city_name] = {"Population": 0, "Gold": 0}
    cities[city_name]["Population"] += int(population)
    cities[city_name]["Gold"] += int(gold)

while True:
    command = input()

    if command == "End":
        break

    command = command.split("=>")
    action = command[0]

    if action == "Plunder":
        plunder(cities, command)

    elif action == "Prosper":
        prosper(cities, command)

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        print(f"{city} -> Population: {info['Population']} citizens, Gold: {info['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
