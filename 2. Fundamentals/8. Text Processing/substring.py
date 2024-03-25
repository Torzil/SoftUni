string_to_remove = input()
string_to_process = input()

while string_to_remove in string_to_process:
    string_to_process = string_to_process.replace(string_to_remove, "")

print(string_to_process)
