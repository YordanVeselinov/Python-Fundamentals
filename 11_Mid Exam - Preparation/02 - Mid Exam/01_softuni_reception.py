employee_efficiency_one = int(input())
employee_efficiency_two = int(input())
employee_efficiency_three = int(input())
students_count = int(input())
per_hour_eff = employee_efficiency_three + employee_efficiency_two + employee_efficiency_one
time = 0
while True:

    if students_count <= 0:
        break
    time += 1
    if time % 4 == 0:
        continue
    students_count -= per_hour_eff

print(f"Time needed: {time}h.")
