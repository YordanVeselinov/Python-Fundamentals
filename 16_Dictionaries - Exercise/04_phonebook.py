my_dict = {}
n = 0
while True:
    line = input()
    if len(line) < 5:
        n = int(line)
        break
    name, phone = line.split("-")
    my_dict[name] = phone
for _ in range(n):
    searched_name = input()
    if searched_name in my_dict.keys():
        print(f"{searched_name} -> {my_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")