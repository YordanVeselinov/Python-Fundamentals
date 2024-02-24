people = int(input())
wagons = [int(num) for num in input().split()]
is_full_wagon = False
for current_index in range(len(wagons)):
    while wagons[current_index] != 4 and people != 0:
        wagons[current_index] += 1
        people -= 1
if sum(wagons) == len(wagons) * 4:
    is_full_wagon = True

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(map(str, wagons)))
elif is_full_wagon and people == 0:
    print(" ".join(map(str, wagons)))
else:
    print(f"The lift has empty spots!")
    print(" ".join(map(str, wagons)))
