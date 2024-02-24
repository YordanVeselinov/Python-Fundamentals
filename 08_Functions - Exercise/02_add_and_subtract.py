def sum_numbers(first,second):
    return first + second


def subtract(result,third):
    return result - third


def add_and_subtract(first,second,third):
    final_result = sum_numbers(first,second)
    return subtract(final_result,third)


first_numbers = int(input())
second_numbers = int(input())
third_numbers = int(input())

print_result = add_and_subtract(first_numbers, second_numbers, third_numbers)
print(print_result)