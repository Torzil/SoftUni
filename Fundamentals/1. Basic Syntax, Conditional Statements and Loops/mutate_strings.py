first_string = input()
second_string = input()
last_string = first_string

for letter in range(len(first_string)):
    right_half = first_string[letter + 1:]
    left_half = second_string[:letter + 1]
    current_string = left_half + right_half
    if current_string != last_string:
        print(current_string)
    last_string = current_string
