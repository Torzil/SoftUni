import re

regex = r"\b(w{3}\.[A-Za-z0-9\-\.]+\.([a-z]+)+)\b"

text = input()
while text:
    result = re.search(regex, text)
    if result:
        url = result.group(1)
        print(url)
    text = input()
