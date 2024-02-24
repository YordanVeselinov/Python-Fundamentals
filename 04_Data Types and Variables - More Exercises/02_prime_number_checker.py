num = int(input())
is_prime = False
if num > 1:
    for i in range(2, int(num/2)+1):

        if (num % i) == 0:
            break
    else:
        is_prime = True
print(is_prime)