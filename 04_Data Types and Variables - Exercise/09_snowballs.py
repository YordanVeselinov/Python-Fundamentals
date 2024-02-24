number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for current_snowball in range(number_of_snowballs):
    weights_of_snowballs = int(input())
    time_of_snowball = int(input())
    quantity_of_snowballs = int(input())
    value = (weights_of_snowballs / time_of_snowball) ** quantity_of_snowballs
    if value > max_value:
        max_value = value
        max_quality = quantity_of_snowballs
        max_time = time_of_snowball
        max_weight = weights_of_snowballs

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")