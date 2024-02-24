def orders(name_of_product:str,quantity_of_product:int) -> float:
    price = 0
    if name_of_product == "coffee":
        price = quantity_of_product * 1.50
    elif name_of_product == "water":
        price = quantity_of_product * 1.00
    elif name_of_product == "coke":
        price = quantity_of_product * 1.40
    elif name_of_product == "snacks":
        price = quantity_of_product * 2.00
    return price






product = input()
quantity = int(input())
result = orders(product, quantity)
print(f"{result:.2f}")


