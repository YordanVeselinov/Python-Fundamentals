def positive_number(list_of_numbers):
    return [str(positive) for positive in list_of_numbers if positive >= 0]


def negative_number(list_of_numbers):
    return [str(negative) for negative in list_of_numbers if negative < 0]


def odd_number(list_of_numbers):
    return [str(odd) for odd in list_of_numbers if odd % 2 != 0]


def even_number(list_of_numbers):
    return [str(even) for even in list_of_numbers if even % 2 == 0]


numbers = [int(x) for x in input().split(", ")]
positive = positive_number(numbers)
negative = negative_number(numbers)
odd = odd_number(numbers)
even = even_number(numbers)
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")