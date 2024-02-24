numbers = input().split(", ")
beggars = int(input())
list_of_numbers = []
for i in numbers:
    list_of_numbers.append(int(i))
index = 0
total_amount = []
for current_beggar in range(beggars):
    current_beggar_amount = 0
    for index_for_amount in range(index ,len(list_of_numbers), beggars):
        current_beggar_amount += list_of_numbers[index_for_amount]
    index += 1
    total_amount.append(current_beggar_amount)
print(total_amount)