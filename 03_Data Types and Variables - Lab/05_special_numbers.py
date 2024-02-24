n = int(input())
sum_digits = 0
for current_num in range(1, n + 1):
    current_num_as_str = str(current_num)
    sum_digits = 0
    for digit in current_num_as_str:
        sum_digits += int(digit)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{current_num} -> True")
    else:
        print(f"{current_num} -> False")


