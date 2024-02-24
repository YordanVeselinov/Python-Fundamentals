numbers = [int(num) for num in input().split(", ")]
index_list = []
for number in numbers:
    if number % 2 == 0:
        index_list.append(numbers.index(number))

print(index_list)