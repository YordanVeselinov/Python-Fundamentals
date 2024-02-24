budget = float(input())
price_per_kg_flour = float(input())
one_pack_eggs = price_per_kg_flour * 0.75
liter_price_milk = (price_per_kg_flour * 1.25)
one_quarter_milk_price = liter_price_milk / 4

price_for_one_bread = price_per_kg_flour + one_pack_eggs + one_quarter_milk_price
made_breads = 0
total_cost_breads = 0
colored_eggs = 0
while True:
    price_for_one_bread += total_cost_breads
    budget -= price_for_one_bread
    made_breads += 1
    colored_eggs += 3
    if made_breads % 3 == 0:
        colored_eggs -= (made_breads - 2)
    if budget < price_for_one_bread:
        break

print(f"You made {made_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
