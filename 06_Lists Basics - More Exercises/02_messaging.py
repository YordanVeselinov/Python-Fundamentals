numbers = input().split()
message = list(input())
string = ""

for numbers in numbers:
    sum_of_index = 0
    for current_num in numbers:
        sum_of_index += int(current_num)
    if sum_of_index >= len(message):
        sum_of_index -= len(message)
        string += message[sum_of_index]
        message.remove(message[sum_of_index])
    else:
        string += message[sum_of_index]
        message.remove(message[sum_of_index])
print(string)

