import re

text = input()

threshold_pattern = r"\d"
emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

threshold_numbers = re.findall(threshold_pattern, text)
threshold = int(threshold_numbers[0])
threshold_numbers.remove(threshold_numbers[0])
for num in threshold_numbers:
    threshold *= int(num)

valid_emojis = re.findall(emoji_pattern, text)
cool_emojis = []
for item in valid_emojis:
    emoji = item[1]
    emoji_coolness = 0
    for char in emoji:
        emoji_coolness += ord(char)
    if emoji_coolness >= threshold:
        cool_emojis.append(f"{item[0]}{emoji}{item[0]}")

number_of_emojis = len(valid_emojis)
number_of_cool_emojis = len(cool_emojis)

print(f"Cool threshold: {threshold}")
print(f"{number_of_emojis} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojis:
    print(cool_emoji)
