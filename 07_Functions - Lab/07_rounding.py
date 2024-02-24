def rounding(number:float) -> int:
    result = round(number)
    return result


float_numbers_list = [float(number) for number in input().split()]
int_numbers_list = []

for current_number in float_numbers_list:
    int_numbers_list.append(rounding(current_number))
print(int_numbers_list)