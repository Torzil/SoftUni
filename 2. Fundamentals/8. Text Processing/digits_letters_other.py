initial_string = input()
numbers = ""
letters = ""
others = ""

for char in initial_string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(numbers)
print(letters)
print(others)
