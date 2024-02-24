import re
pattern = r"([=\/])([A-Z][a-zA-Z]{2,})\1"
destinations = input()
matches = re.findall(pattern,destinations)
travel_points = sum([len(destination[1]) for destination in matches])
join_matches = [destination[1] for destination in matches]
print(f"Destinations: {', '.join(join_matches)}")
print(f"Travel Points: {travel_points}")
