first_range = int(input())
second_range = int(input())

for current_range in range(first_range, second_range + 1):
    letter = chr(current_range)
    if current_range == second_range:
        print(letter)
    else:
        print(letter , end=' ')