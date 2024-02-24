products_list = input().split()
dict_products = {}
for i in range(0,len(products_list),2):
    key = products_list[i]
    value = int(products_list[i+1])
    dict_products[key] = value
needed_products = input().split()

for current_product in needed_products:
    if current_product in dict_products:
        print(f"We have {dict_products[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")