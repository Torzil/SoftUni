initial_string = input()
filtered_string = ""
last_char = ""

for char in initial_string:
    if char != last_char:
        filtered_string += char
    last_char = char

print(filtered_string)
