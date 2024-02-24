def calculator(operation=str,first=int,second=int):
    if operation == "multiply":
        result = first * second
    elif operation == "divide":
        result = first // second
    elif operation == "add":
        result = first + second
    elif operation == "subtract":
        result = first - second
    return result




operator = input()
first_value = int(input())
second_value = int(input())
outcome = calculator(operator,first_value, second_value)
print(outcome)
