numbers = input().split(' ')
list_of_numbers = []

for element in numbers:
    reverse_number = -int(element)
    list_of_numbers.append(reverse_number)
print(list_of_numbers)