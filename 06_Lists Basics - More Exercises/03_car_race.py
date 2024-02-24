list_of_number = input().split()
middle = int(len(list_of_number) / 2)
left_part = list_of_number[0:middle]
right_part = list_of_number[middle+1:]
sum_left = 0
sum_right = 0

for current_left_number in left_part:
    if int(current_left_number) == 0:
        sum_left *= 0.80
    else:
        sum_left += int(current_left_number)
for current_right_number in right_part[::-1]:
    if int(current_right_number) == 0:
        sum_right *= 0.80
    else:
        sum_right += int(current_right_number)

if sum_left < sum_right:
    print(f'The winner is left with total time: {sum_left:.1f}')
else:
    print(f'The winner is right with total time: {sum_right:.1f}')