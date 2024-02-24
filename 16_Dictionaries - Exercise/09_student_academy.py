n = int(input())
students_academy = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students_academy.keys():
        students_academy[name] = []
    students_academy[name].append(grade)
for key , value in students_academy.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")
    else:
        continue