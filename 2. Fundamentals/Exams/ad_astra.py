import re

text = input()
total_calories = 0
foodstuffs = []

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.finditer(pattern, text)

for match in matches:
    food = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))
    foodstuffs.append([food, expiration_date, calories])
    total_calories += calories

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")

for foodstuff in foodstuffs:
    print(f"Item: {foodstuff[0]}, Best before: {foodstuff[1]}, Nutrition: {foodstuff[2]}")
