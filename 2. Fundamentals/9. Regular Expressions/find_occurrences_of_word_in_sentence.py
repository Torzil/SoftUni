import re

text = input()
searched_word = input()

regex = fr"\b{searched_word}\b"

result = re.findall(regex, text, re.IGNORECASE)

print(len(result))
