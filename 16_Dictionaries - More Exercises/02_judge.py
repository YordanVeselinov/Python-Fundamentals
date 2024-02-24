from collections import defaultdict

contests = defaultdict(dict)
individual_stats = defaultdict(int)

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if username not in contests[contest]:
        contests[contest][username] = points
        individual_stats[username] += points
    else:
        if points > contests[contest][username]:
            individual_stats[username] += points - contests[contest][username]
            contests[contest][username] = points

sorted_contests = dict(sorted(contests.items(), key=lambda x: x[0]))

for contest, participants in sorted_contests.items():
    print(f"{contest}: {len(participants)} participants")
    position = 1
    for user, points in sorted(participants.items(), key=lambda x: (-x[1], x[0])):
        print(f"{position}. {user} <::> {points}")
        position += 1

print("Individual standings:")
position = 1
for user, total_points in sorted(individual_stats.items(), key=lambda x: (-x[1], x[0])):
    print(f"{position}. {user} -> {total_points}")
    position += 1
