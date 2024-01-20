from math import inf

numbers_amount = int(input())

max_number = -inf
total_sum = 0
final_sum = 0

for number in range(numbers_amount):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

final_sum = total_sum - max_number
difference = abs(max_number - final_sum)

if max_number == final_sum:
    print("Yes")
    print(f"Sum = {final_sum}")
else:
    print("No")
    print(f"Diff = {difference}")
