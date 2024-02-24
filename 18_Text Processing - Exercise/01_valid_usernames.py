def valid_length(password):
    if 3 <= len(password) <= 16:
        return True
    return False


def characters_are_valid(password):
    for character in password:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(password):
    if " " in password:
        return False
    return True


def username_is_valid(password):
    if valid_length(password) and characters_are_valid(password) and no_redundant_symbols(password):
        return True
    return False


passwords = input().split(", ")
valid_passwords = []

for password in passwords:
    if username_is_valid(password):
        print(password)