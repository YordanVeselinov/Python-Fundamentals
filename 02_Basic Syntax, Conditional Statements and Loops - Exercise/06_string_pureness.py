string_number = int(input())

for current_string in range(string_number):
    input_string = input()
    if "," in input_string or \
        "." in input_string or \
        "_" in input_string:
        print(f"{input_string} is not pure!")
    else:
        print(f"{input_string} is pure.")
        