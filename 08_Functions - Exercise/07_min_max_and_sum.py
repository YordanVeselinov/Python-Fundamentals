def max_num(number:list)-> int:
    return max(number)


def min_num(number:list)-> int:
    return min(number)


def sum_of_numbers(number:list)-> int:
    return sum(number)



list_of_number = [int(number) for number in input().split()]
minimum = min_num(list_of_number)
maximum = max_num(list_of_number)
sum_numbers = sum_of_numbers(list_of_number)

print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {sum_numbers}")
