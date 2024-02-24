quantity_food_kilograms = float(input()) * 1000
quantity_hay_kilograms = float(input()) * 1000
quantity_cover_kilograms = float(input()) * 1000
weith_kilograms = float(input()) * 1000
is_food_not_enoug = False

for i in range(1,31):
    quantity_food_kilograms -= 300
    if i % 2 == 0:
        quantity_hay_kilograms -= 0.05 * quantity_food_kilograms
    if i % 3 == 0:
        quantity_cover_kilograms -= weith_kilograms / 3
    if quantity_food_kilograms <= 0 or quantity_hay_kilograms <= 0 or quantity_cover_kilograms <= 0:
        is_food_not_enoug = True
        break
if is_food_not_enoug:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_kilograms / 1000:.2f}, Hay: {quantity_hay_kilograms / 1000:.2f}, Cover: {quantity_cover_kilograms / 1000:.2f}.")
