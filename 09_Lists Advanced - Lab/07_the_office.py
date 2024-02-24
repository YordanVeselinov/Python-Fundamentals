employees = [int(num) for num in input().split()]
happines_factor = int(input())

empowared_employees = [num * happines_factor for num in employees]
length_of_employees = len(employees)
average_happines = sum(empowared_employees) / length_of_employees
happy_employees = len([happy_number for happy_number in empowared_employees if happy_number >= average_happines])

if happy_employees >= length_of_employees / 2:
    print(f"Score: {happy_employees}/{length_of_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{length_of_employees}. Employees are not happy!")