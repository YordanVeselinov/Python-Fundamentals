food_list = input().split()
food_dict = {}

for index in range(0, len(food_list), 2):
    key = food_list[index]
    value = int(food_list[index + 1])
    food_dict[key] = value
print(food_dict)
