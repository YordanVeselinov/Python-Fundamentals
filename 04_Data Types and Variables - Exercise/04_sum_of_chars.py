numbers = int(input())
total_sum = 0
for current_number in range(numbers):
    digit = input()
    total_sum += ord(digit)

print(f"The sum equals: {total_sum}")


