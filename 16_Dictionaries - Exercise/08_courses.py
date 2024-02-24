course_dict = {}
while True:
    line = input().split(" : ")
    if line[0] == "end":
        break
    course = line[0]
    name = line[1]
    if course not in course_dict.keys():
        course_dict[course] = []
    course_dict[course].append(name)

for key, value in course_dict.items():
    print(f"{key}: {len(value)}")
    for current_name in value:
        print(f"-- {current_name}")
