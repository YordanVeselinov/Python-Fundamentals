cities = {}

while True:
    line = input()
    if line == "Sail":
        break
    city, population, gold = line.split("||")
    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += int(population)
    cities[city]["gold"] += int(gold)

while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)
    elif action == "Prosper":
        town, gold = command[1], int(command[2])
        if gold >= 0:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, population_gold in cities.items():
        print(f"{city} -> Population: {population_gold['population']} citizens, Gold: {population_gold['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


