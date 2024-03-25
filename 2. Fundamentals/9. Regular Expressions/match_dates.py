import re

text = input()

regex = r"\b(\d{2})(\/|\-|\.)([A-Z]{1}[a-z]{2})\2(\d{4})\b"

result = re.findall(regex, text)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
