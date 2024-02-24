n = int(input())
parking_lot = {}
for _ in range(n):
    line = input().split()
    command = line[0]
    name = line[1]
    if len(line) > 2:
        registration_plate = line[2]
    if command == "unregister" and name in parking_lot.keys():
        parking_lot.pop(name)
        print(f"{name} unregistered successfully")
    elif command == "unregister" and name not in parking_lot.keys():
        print(f"ERROR: user {name} not found")
    if command == "register" and name not in parking_lot.keys():
        parking_lot[name] = registration_plate
        print(f"{name} registered {registration_plate} successfully")
    elif command == "register" and name in parking_lot.keys():
        print(f"ERROR: already registered with plate number {registration_plate}")


for key, value in parking_lot.items():
    print(f"{key} => {value}")

