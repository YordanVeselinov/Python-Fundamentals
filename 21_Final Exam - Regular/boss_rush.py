import re
number_of_bosses = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

# Group 1 = Boss name
# Group 2 = Title
for boss in range(number_of_bosses):
    current_boss = input()
    match = re.match(pattern, current_boss)
    if match:
        boss_name, title = match.group(1), match.group(2)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print(f"Access denied!")