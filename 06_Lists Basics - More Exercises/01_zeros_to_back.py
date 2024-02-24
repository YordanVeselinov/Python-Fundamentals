list_of_numbers = input().split(', ')
integer_list = []

for current_number in list_of_numbers:
    if current_number == "0":
        list_of_numbers.remove(current_number)
        list_of_numbers.append(current_number)
for integer in list_of_numbers:
    integer_list.append(int(integer))



print(integer_list)