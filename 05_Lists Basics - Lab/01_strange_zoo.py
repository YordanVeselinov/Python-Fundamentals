# tail = input()
# body = input()
# head = input()
# my_list = []
#
# my_list.append(head)
# my_list.append(body)
# my_list.append(tail)
# print(my_list)

my_list = []
for _ in range(3):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)