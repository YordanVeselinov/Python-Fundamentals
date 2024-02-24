list_of_types_and_prices = input().split('|')
budget = int(input())
new_prices_list = []
profit = 0


for item in list_of_types_and_prices:
    current_item_list = item.split('->')
    wear = current_item_list[0]
    price = float(current_item_list[1])
    if price <= budget:
        if (wear == "Clothes" and price <= 50) \
            or (wear == "Shoes" and price <= 35.0) \
            or (wear == "Accessories" and price <= 20.50):
            new_prices_list.append(price)
            budget -= price

profit = 0.4 * (sum(new_prices_list))

for item in new_prices_list:
    print(f"{item*1.40:.2f}",end=" ")
print()
print(f"Profit: {profit:.2f}")

total_profit = budget + sum(new_prices_list) * 1.40


if total_profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")