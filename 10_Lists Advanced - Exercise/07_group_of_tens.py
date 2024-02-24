numbers = [int(num) for num in input().split(", ")]
group = 10
while True:
    group_nubers = [num for num in numbers if num <= group]
    if numbers == []:
        break
    print(f"Group of {group}'s: {group_nubers}")
    numbers = [num for num in numbers if num not in group_nubers]
    group += 10