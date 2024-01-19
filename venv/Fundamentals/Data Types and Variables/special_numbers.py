number_input = int(input())

for number in range(1, number_input + 1):
    number_as_string = str(number)
    sum_of_digits = 0
    number_is_special = False
    for digit in number_as_string:
        sum_of_digits += int(digit)
        if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
            number_is_special = True
    print(f"{number} -> {number_is_special}")
