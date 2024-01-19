number_of_strings = int(input())

for string in range(number_of_strings):
    string_is_pure = True
    current_string = input()
    for letter in current_string:
        if letter in ",._":
            string_is_pure = False
            print(f"{current_string} is not pure!")
            break
    if string_is_pure:
        print(f"{current_string} is pure.")
