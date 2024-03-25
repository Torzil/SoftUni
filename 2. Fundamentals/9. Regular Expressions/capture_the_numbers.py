import re

numbers = []
regex = r"\d+"
line = input()
while line:
    result = re.findall(regex, line)
    if result:
        for match in result:
            print(match, end=" ")
    line = input()
