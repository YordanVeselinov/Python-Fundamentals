n = int(input())
input_num = 0

for i in range(n):
    input_num = int(input())
    if input_num % 2 == 1:
        print(f"{input_num} is odd!")
        break
else:
    print("All numbers are even.")


