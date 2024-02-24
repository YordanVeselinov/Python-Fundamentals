def intput_intiger(some_number):
    return some_number * 2


def real_function(some_int_number):
    return f"{some_int_number * 1.5:.2f}"


def string_function(some_string):
    return f"${some_string}$"


command = input()
second_command = input()

if command == "int":
    print(intput_intiger(int(second_command)))
elif command == "real":
    print(real_function(float(second_command)))
elif command == "string":
    print(string_function(second_command))

