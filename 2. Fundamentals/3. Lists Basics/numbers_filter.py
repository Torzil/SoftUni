number_of_integers = int(input())

all_integers = []
filtered_integers = []

for number in range(number_of_integers):
    current_integer = int(input())
    all_integers.append(current_integer)

number_filter = input()

for integer in all_integers:
    if number_filter == "even":
        if integer % 2 == 0:
            filtered_integers.append(integer)
    if number_filter == "odd":
        if integer % 2 != 0:
            filtered_integers.append(integer)
    if number_filter == "negative":
        if integer < 0:
            filtered_integers.append(integer)
    if number_filter == "positive":
        if integer >= 0:
            filtered_integers.append(integer)

print(filtered_integers)
