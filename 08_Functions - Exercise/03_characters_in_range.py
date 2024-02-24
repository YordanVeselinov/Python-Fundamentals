def character_in_range(first:str ,second: str) -> list:
    list_of_characters = []
    for current_charecter in range(ord(first)+1, ord(second)):
        list_of_characters.append(chr(current_charecter))
    return list_of_characters


first_element = input()
second_element = input()
result = character_in_range(first_element, second_element)
print(" ".join(result))
# string = " "
# number = 97
# print(chr(number))
# print(ord(string))