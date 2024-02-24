house = [int(x) for x in input().split("@")]
index = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break
    current_index = int(command[1])
    index += current_index
    if index >= len(house):
        index = 0
    if house[index] != 0:
        house[index] -= 2
        if house[index] == 0:
            print(f"Place {index} has Valentine's day.")
    else:
        print(f"Place {index} already had Valentine's day.")

print(f"Cupid's last position was {index}.")
if sum(house) == 0:
    print("Mission was successful.")
else:
    failed = [failed for failed in house if failed != 0]
    print(f"Cupid has failed {len(failed)} places.")