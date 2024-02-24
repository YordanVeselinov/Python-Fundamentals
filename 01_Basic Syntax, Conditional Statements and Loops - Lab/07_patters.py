counter = int(input())

for i in range(1, counter + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range(counter - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()