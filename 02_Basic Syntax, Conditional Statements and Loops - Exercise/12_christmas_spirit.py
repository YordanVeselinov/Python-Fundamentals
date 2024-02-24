quantity_of_decorations = int(input())
days_until_christmas = int(input())
spirit = 0
total_cost = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += ornament_set * quantity_of_decorations
        spirit += 5
    if day % 3 == 0:
        total_cost += (tree_garland + tree_skirt) * quantity_of_decorations
        spirit += 3 + 10
    if day % 5 == 0:
        total_cost += 15 * quantity_of_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
