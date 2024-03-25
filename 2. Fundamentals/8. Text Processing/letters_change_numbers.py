strings_list = input().split()


def letters_operation(string):
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    else:
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    else:
        number += (ord(last_letter) - 96)
    return number


def number_sum(all_strings):
    total_sum = 0
    for string in all_strings:
        total_sum += letters_operation(string)
    return f"{total_sum:.2f}"


print(number_sum(strings_list))
