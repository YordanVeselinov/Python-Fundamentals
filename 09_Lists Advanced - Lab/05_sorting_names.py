names = input().split(", ")

filtered_names = sorted(names, key=lambda name: (-len(name),name))
print(filtered_names)