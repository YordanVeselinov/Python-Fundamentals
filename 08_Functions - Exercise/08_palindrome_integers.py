def palindrome_integer(number:str) -> bool:
    if number == number[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")

for current_number in list_of_numbers:
    print(palindrome_integer(current_number))