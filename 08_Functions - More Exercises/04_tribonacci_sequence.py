def tribonacci(n):
    if n <= 0:
        return []

    tribonacci_sequence = [1]

    if n == 1:
        return tribonacci_sequence

    tribonacci_sequence.append(1)

    if n == 2:
        return tribonacci_sequence

    tribonacci_sequence.append(2)

    if n == 3:
        return tribonacci_sequence

    for i in range(3, n):
        next_num = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        tribonacci_sequence.append(next_num)

    return tribonacci_sequence


num = int(input())

sequence = tribonacci(num)


print(*sequence)
