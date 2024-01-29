number_of_strings = int(input())
filter_word = input()

all_strings = []
filtered_strings = []

for string in range(number_of_strings):
    current_string = input()
    all_strings.append(current_string)
    if filter_word in current_string:
        filtered_strings.append(current_string)

print(all_strings)
print(filtered_strings)
