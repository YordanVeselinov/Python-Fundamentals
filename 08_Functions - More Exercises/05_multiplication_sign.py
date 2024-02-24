def determine_multiplication_sign(a, b, c):
    count_negatives = 0

    if a < 0:
        count_negatives += 1
    if b < 0:
        count_negatives += 1
    if c < 0:
        count_negatives += 1

    if count_negatives % 2 == 0:
        return "positive"
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())


result = determine_multiplication_sign(num1, num2, num3)


print(result)
