import re

text = input()

regex = r"\s(([a-z0-9]+)([a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"

extracted_emails = re.findall(regex, text)

for email in extracted_emails:
    print(email[0])
