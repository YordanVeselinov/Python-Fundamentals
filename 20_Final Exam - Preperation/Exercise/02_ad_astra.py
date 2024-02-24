import re
food_info = input()
pattern = r"([|#])([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.findall(pattern,food_info)
total_calories = sum([int(match[3])for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
