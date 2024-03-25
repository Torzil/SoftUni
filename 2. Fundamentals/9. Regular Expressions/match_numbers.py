import re

text = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = re.finditer(regex, text)

for match in result:
    print(match.group(), end=" ")
