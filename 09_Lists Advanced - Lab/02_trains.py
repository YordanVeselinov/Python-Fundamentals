wagons = [0] * int(input())
command = input().split()

while command[0] != "End":
    if command[0] == "add":
        people = int(command[1])
        wagons[-1] += people
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people

    command = input().split()

print(wagons)
