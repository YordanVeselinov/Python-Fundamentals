def perfect_number(some_number):
    sum_number = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            sum_number += current_number
    return sum_number == some_number




number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")