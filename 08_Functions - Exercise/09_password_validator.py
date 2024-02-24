def password_validator(some_password: str):
    list_of_errors = []
    if not 6 <= len(some_password) <= 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for element in some_password:
        if element.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")

    return list_of_errors


password = input()
validate_password = password_validator(password)
if len(validate_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validate_password))
