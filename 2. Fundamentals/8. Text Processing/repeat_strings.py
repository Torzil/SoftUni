strings_list = input().split()
repeated_strings = ""

for string in strings_list:
    repeated_strings += string * len(string)

print(repeated_strings)
