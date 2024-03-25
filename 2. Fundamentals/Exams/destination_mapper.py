import re

destinations = input()
valid_destinations = []
travel_points = 0

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(pattern, destinations)

for match in matches:
    valid_destinations.append(match.group(2))
    travel_points += len(match.group(2))

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")