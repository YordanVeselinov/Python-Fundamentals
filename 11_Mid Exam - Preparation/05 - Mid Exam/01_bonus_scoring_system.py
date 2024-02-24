number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
max_attendance = 0

for current_student in range(number_of_students):
    attendances = int(input())
    bonus_points = attendances / total_number_of_lectures * (5 + additional_bonus)
    if bonus_points > max_bonus_points:
        max_bonus_points = bonus_points
        max_attendance = attendances
print(f"Max Bonus: {round(max_bonus_points)}.")
print(f"The student has attended {round(max_attendance)} lectures.")
