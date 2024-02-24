animals = {}
areas = {}

while True:
    command = input()
    if command == "EndDay":
        break
    action, animal_information = command.split(": ")
    if action == "Add":
        animal, needed_food, area = animal_information.split("-")
        if animal not in animals:
            animals[animal] = {"needed_food": 0, "area": area}
        animals[animal]["needed_food"] += int(needed_food)
        if area not in areas:
            areas[area] = {"animals": []}
        if animal not in areas[area]["animals"]:
            areas[area]["animals"].append(animal)

    elif action == "Feed":
        animal, add_food = animal_information.split("-")
        if animal in animals.keys():
            animals[animal]["needed_food"] -= int(add_food)
            if animals[animal]["needed_food"] <= 0:
                print(f"{animal} was successfully fed")
                area = animals[animal]["area"]
                animals.pop(animal)
                areas[area]["animals"].remove(animal)
print(f"Animals:")
for animal, needed_food_area in animals.items():
    print(f"{animal} -> {needed_food_area['needed_food']}g")
print("Areas with hungry animals:")
for area in areas:
    if areas[area]['animals']:
        print(f"{area}: {len(areas[area]['animals'])}")

