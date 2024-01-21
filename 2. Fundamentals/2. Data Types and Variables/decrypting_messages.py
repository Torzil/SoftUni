key = int(input())
number_of_lines = int(input())
message = ""

for line in range(number_of_lines):
    current_letter = input()
    message += chr(ord(current_letter) + key)

print(message)
