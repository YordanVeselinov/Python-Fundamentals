contests = {}
submissions = {}


while True:
    data = input()
    if data == "end of contests":
        break
    contest, password = data.split(':')
    contests[contest] = password


while True:
    submission = input()
    if submission == "end of submissions":
        break
    contest, password, username, points = submission.split("=>")
    points = int(points)
    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username]:
            submissions[username][contest] = points
        else:
            submissions[username][contest] = max(submissions[username][contest], points)

best_candidate = max(submissions, key=lambda x: sum(submissions[x].values()))
total_points = sum(submissions[best_candidate].values())

print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")

for user in sorted(submissions.keys()):
    print(user)
    for contest, points in sorted(submissions[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
