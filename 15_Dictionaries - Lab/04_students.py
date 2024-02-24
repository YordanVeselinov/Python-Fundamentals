searched_course = ""
dict_with_students = []
while True:
    line = input().split(":")
    if len(line) < 2:
        searched_course = line[0]
        break
    dict_with_students.append({"name": line[0], "id": line[1],"course": line[2]})
for current_student in dict_with_students:
    if current_student["course"][0:4] == searched_course[0:4]:
        name = current_student["name"]
        id_student = current_student["id"]
        print(f"{name} - {id_student}")