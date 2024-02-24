products = {}
while True:
    line = input().split()
    if line[0] == "buy":
        break
    current_product = line[0]
    price = float(line[1])
    quantity = int(line[2])
    if current_product not in products.keys():
        products[current_product] = []
    if len(products[current_product]) == 0:
        products[current_product].append(price)
        products[current_product].append(quantity)
    else:
        products[current_product][0] = price
        products[current_product][1] += quantity

for key, value in products.items():
    price = value[0]
    quantity = value[1]
    result = price * quantity
    print(f"{key} -> {result:.2f}")