def sorting(numbers: list) -> list:
    numbers.sort()
    return numbers



number_as_list = [int(number) for number in input().split()]
result = sorting(number_as_list)
print(result)