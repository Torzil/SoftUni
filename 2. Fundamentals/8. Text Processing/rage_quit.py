rage_string = input()
rage_message = ""
current_string = ""
repetitions = ""

for index in range(len(rage_string)):
    character = rage_string[index]
    if character.isdigit():
        for next_index in range(index, len(rage_string)):
            if not rage_string[next_index].isdigit():
                break
            repetitions += rage_string[next_index]
        rage_message += current_string * int(repetitions)
        current_string = ""
        repetitions = ""
    else:
        current_string += character.upper()


unique_symbols = len(set(rage_message))

print(f"Unique symbols used: {unique_symbols}")
print(rage_message)
