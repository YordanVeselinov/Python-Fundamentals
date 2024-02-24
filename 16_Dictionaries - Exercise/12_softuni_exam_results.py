results = {}
submissions = {}

while True:
    line = input()
    if "-" not in line:
        break
    line = line.split("-")
    if len(line) > 2:
        name, course, points = line
        points = int(points)
        if name not in results:
            results[name] = 0
        if course not in submissions:
            submissions[course] = 0
        submissions[course] += 1
        if results[name] < points:
            results[name] = points
    else:
        name, banned = line
        results.pop(name)

print("Results:")
for key, value in results.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
