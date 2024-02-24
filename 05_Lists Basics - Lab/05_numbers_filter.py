numbers = int(input())
list_of_numbers = []
for _ in range(numbers):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()
list_for_print = []

for current_number in list_of_numbers:
    if command == 'even':
        if current_number % 2 == 0:
            list_for_print.append(current_number)
    if command == 'odd':
        if current_number % 2 != 0:
            list_for_print.append(current_number)
    if command == 'positive':
        if current_number >= 0:
            list_for_print.append(current_number)
    if command == 'negative':
        if current_number < 0:
            list_for_print.append(current_number)
print(list_for_print)

