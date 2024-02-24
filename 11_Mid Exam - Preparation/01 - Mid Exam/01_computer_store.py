total_without_taxes = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue
    total_without_taxes += price

taxes = total_without_taxes * 0.20
price_with_taxes = taxes + total_without_taxes
if command == "special":
    price_with_taxes = price_with_taxes * 0.90

if total_without_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")
