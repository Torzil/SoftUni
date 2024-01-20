string = input()
while string != "End":
    string_is_valid = True
    for letter in string:
        if string == "SoftUni":
            string_is_valid = False
            break
        print(letter + letter, end='')
    if string_is_valid:
        print()
    string = input()
