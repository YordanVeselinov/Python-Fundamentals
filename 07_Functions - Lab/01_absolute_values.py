list_of_absolute_values = []
def absolute_values(some_number:float) -> float:
    list_of_absolute_values.append(float(abs(some_number)))
    return list_of_absolute_values



numbers = input().split()

for current_number_as_string in numbers:
    absolute_values(float(current_number_as_string))

print(list_of_absolute_values)