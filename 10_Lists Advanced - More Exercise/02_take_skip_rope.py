def extract_hidden_message(input_str):
    numbers = [int(char) for char in input_str if char.isdigit()]
    non_numbers = [char for char in input_str if not char.isdigit()]

    take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

    result = ""
    idx = 0

    for i in range(len(take_list)):
        take_chars = take_list[i]
        skip_chars = skip_list[i] if i < len(skip_list) else 0

        result += ''.join(non_numbers[idx:idx + take_chars])
        idx += take_chars + skip_chars

    print(result)


input_string = input()

extract_hidden_message(input_string)
