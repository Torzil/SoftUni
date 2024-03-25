number_of_plants = int(input())
plant_collection = {}

for new_plant in range(number_of_plants):
    current_plant, rarity = input().split('<->')
    if current_plant not in plant_collection:
        plant_collection[current_plant] = {"Rarity:": 0, "Rating:": []}
    plant_collection[current_plant]["Rarity:"] = rarity

while True:
    command = input()
    if command == 'Exhibition':
        break
    command = command.split()
    action = command[0]
    plant = command[1]
    if plant not in plant_collection:
        print("error")
        continue
    if action == "Rate:":
        rating = int(command[3])
        plant_collection[plant]["Rating:"].append(rating)
    elif action == "Update:":
        rarity = int(command[3])
        plant_collection[plant]["Rarity:"] = rarity
    elif action == "Reset:":
        plant_collection[plant]["Rating:"] = []

print("Plants for the exhibition:")
for key in plant_collection.keys():
    current_rarity = plant_collection[key]["Rarity:"]
    current_rating = plant_collection[key]["Rating:"]
    if not plant_collection[key]["Rating:"]:
        average_rating = 0
    else:
        average_rating = sum(current_rating) / len(current_rating)
    print(f"- {key}; Rarity: {current_rarity}; Rating: {average_rating:.2f}")
