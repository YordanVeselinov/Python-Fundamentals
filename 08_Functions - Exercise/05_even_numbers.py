def even_numbers(numbers:list) -> list:
    result_numbers = []
    for current_number in numbers:
        if current_number % 2 == 0:
            result_numbers.append(current_number)
    return result_numbers


list_of_numbers = [int(numbers) for numbers in input().split()]
result = even_numbers(list_of_numbers)
print(result)