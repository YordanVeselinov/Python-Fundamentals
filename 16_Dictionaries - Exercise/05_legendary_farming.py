materials = {"shards": 0, "fragments": 0, "motes": 0}
winner_string = ""
is_abtained = False

while True:
    materials_quantity = input().split()
    for index in range(0, len(materials_quantity), 2):
        quantity = int(materials_quantity[index])
        material = materials_quantity[index + 1].lower()
        if material not in materials.keys():
            materials[material] = 0
        materials[material] += quantity
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            winner_string = "Shadowmourne obtained!"
            is_abtained = True
            break
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            winner_string = "Valanyr obtained!"
            is_abtained = True
            break
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            winner_string = "Dragonwrath obtained!"
            is_abtained = True
            break
    if is_abtained:
        break

print(winner_string)
for key, value in materials.items():
    print(f"{key}: {value}")
