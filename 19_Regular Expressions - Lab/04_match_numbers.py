import re

pattern = r"^(?!.*[^\d\s.-]|.*\d.*\d)[+-]?\d+(?:\.\d+)?$"
numbers = input()

matches = re.findall(pattern, numbers)
for match in matches:
    print(f"{match}", end=" ")