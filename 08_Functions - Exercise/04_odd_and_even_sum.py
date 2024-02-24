def odd_sum(numbers):
    result_odd = 0
    for current_number in numbers:
        if int(current_number) % 2 == 0:
            result_odd += int(current_number)
    return result_odd


def even_sum(numbers):
    result_even = 0
    for current_number in numbers:
        if int(current_number) % 2 != 0:
            result_even += int(current_number)
    return result_even


numbers_as_string = input()
odd = odd_sum(numbers_as_string)
even = even_sum(numbers_as_string)

print(f"Odd sum = {even}, Even sum = {odd}")