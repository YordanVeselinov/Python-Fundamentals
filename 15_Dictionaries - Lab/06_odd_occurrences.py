word = input().split()
my_dict = {}

for current in word:
    current_lower = current.lower()
    if current_lower not in my_dict:
        my_dict[current_lower] = 0
    my_dict[current_lower] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=' ')