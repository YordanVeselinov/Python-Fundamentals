numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
new_list = [i for i in numbers[::-1] if i > average]
new_list.sort(key=lambda x: x, reverse=True)
if not new_list:
    print("No")
else:
    print(" ".join(map(str, new_list[:5])))