import re

text = input()
mirror_words = []
number_of_pairs = 0

pattern = r"(#|@)([A-za-z]{3,})\1\1([A-za-z]{3,})\1"

matches = re.finditer(pattern, text)

for match in matches:
    number_of_pairs += 1
    if match.group(2) == match.group(3)[::-1]:
        mirror_words.append(f"{match.group(2)} <=> {match.group(3)}")

if number_of_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{number_of_pairs} word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))
