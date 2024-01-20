interval_start = input()
interval_end = input()
letter_to_skip = input()
valid_combination_counter = 0

for char1 in range(ord(interval_start), ord(interval_end) + 1):
    for char2 in range(ord(interval_start), ord(interval_end) + 1):
        for char3 in range(ord(interval_start), ord(interval_end) + 1):
            if chr(char1) != letter_to_skip and chr(char2) != letter_to_skip \
                    and chr(char3) != letter_to_skip:
                print(f"{chr(char1)}{chr(char2)}{chr(char3)}", end=" ")
                valid_combination_counter += 1
print(valid_combination_counter, end=" ")
