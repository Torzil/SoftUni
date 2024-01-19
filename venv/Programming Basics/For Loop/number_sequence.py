from sys import maxsize

amount_of_numbers = int(input())

max_number = -maxsize
min_number = maxsize

for i in range(0, amount_of_numbers):
    number = int(input())
    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
