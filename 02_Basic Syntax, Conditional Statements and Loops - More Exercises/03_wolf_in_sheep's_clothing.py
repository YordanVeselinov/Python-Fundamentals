queue = []
for i in input().split(", "):
    queue.append(i)

for index in range(-1 ,-(len(queue)+ 1), -1):
    if queue[index] == "wolf" and index == -1:
        print("Please go away and stop eating my sheep")
    elif queue[index] == "wolf" and index != -1:
        print(f"Oi! Sheep number {abs(index)-1}! You are about to be eaten by a wolf!")



