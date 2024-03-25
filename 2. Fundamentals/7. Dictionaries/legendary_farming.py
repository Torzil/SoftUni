def mats_sorter():
    legendary_item = ""
    collected_materials = {"shards": 0, "fragments": 0, "motes": 0}
    collected_junk = {}
    while True:
        if legendary_item != "":
            break
        farmed_items = input().split()
        for index in range(0, len(farmed_items), 2):
            quantity = int(farmed_items[index])
            material = farmed_items[index + 1].lower()
            if material in "shards, fragments, motes":
                collected_materials[material] += quantity
                if collected_materials[material] >= 250:
                    legendary_item = procure_legendary_item(material)
                    collected_materials[material] -= 250
                    break
            else:
                if material not in collected_junk:
                    collected_junk[material] = 0
                collected_junk[material] += quantity
    return collected_materials, collected_junk, legendary_item


def procure_legendary_item(mat):
    legendary_item = ""
    if mat == "shards":
        legendary_item = "Shadowmourne"
    elif mat == "fragments":
        legendary_item = "Valanyr"
    elif mat == "motes":
        legendary_item = "Dragonwrath"
    return legendary_item


mats, junk, legendary = mats_sorter()

print(f"{legendary} obtained!")
for key1, value1 in mats.items():
    print(f"{key1}: {value1}")
for key2, value2 in junk.items():
    print(f"{key2}: {value2}")
