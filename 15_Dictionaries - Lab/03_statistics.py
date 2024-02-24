products = {}
while True:
    line = input().split(": ")
    if line[0] == "statistics":
        break
    key = line[0]
    value = int(line[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value
total_products = len(products)
total_quantity = 0
for key, value in products.items():
    total_quantity += value

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
