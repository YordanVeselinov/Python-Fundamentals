number_of_plants = int(input())
plants = {}
for _ in range(number_of_plants):
    current_plant, current_rarity = input().split("<->")
    if current_plant not in plants:
        plants[current_plant] = {"rarity": 0, "rating": []}
    plants[current_plant]["rarity"] = int(current_rarity)
while True:
    command = input().split(": ")
    if command[0] == "Exhibition":
        break
    action = command[0]
    if action == "Rate":
        plant, rating = command[1].split(" - ")
        rating = int(rating)
        if plant in plants.keys():
            plants[plant]["rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants.keys():
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant = command[1]
        if plant in plants.keys():
            plants[plant]["rating"] = []
        else:
            print("error")
print("Plants for the exhibition:")
for plant, rarity_rating in plants.items():
    if sum(rarity_rating["rating"]) == 0 or len(rarity_rating["rating"]) == 0:
        average = 0
    else:
        average = sum(rarity_rating["rating"]) / len(rarity_rating["rating"])
    print(f"- {plant}; Rarity: {rarity_rating['rarity']}; Rating: {average:.2f}")

