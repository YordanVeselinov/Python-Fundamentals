resorses = {}
counter = 0
while True:
    counter += 1
    line = input()
    if line == "stop":
        break

    if counter % 2 != 0:
        material = line
        if material not in resorses:
            resorses[material] = 0
    elif counter % 2 == 0:
        quantity = int(line)
        resorses[material] += quantity

for key,value in resorses.items():
    print(f"{key} -> {value}")