import sys
list_of_numbers = input().split()
removed_numbers = int(input())

for removed in range(removed_numbers):
    smallest_number = sys.maxsize
    for current_number in list_of_numbers:
        current_number = int(current_number)
        if current_number < smallest_number:
            smallest_number = current_number
    list_of_numbers.remove(str(smallest_number))

print(", ".join(list_of_numbers))